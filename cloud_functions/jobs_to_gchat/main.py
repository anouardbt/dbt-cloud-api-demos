import hashlib
import hmac
import json
import re
import os
import requests
from flask import abort, jsonify

# Access secret credentials from environment variables
HOOK_SECRET = os.getenv('DBT_WEBHOOK_KEY')
API_TOKEN = os.getenv('DBT_CLOUD_SERVICE_TOKEN')
DBT_API_URL = os.getenv('DBT_API_URL', 'https://c1.us1.dbt.com/api/v2')
GOOGLE_CHAT_WEBHOOK_URL = os.getenv('GOOGLE_CHAT_WEBHOOK_URL', 'example_webhook_url')

def http_function(request):
    # Validate that secrets are set
    if not HOOK_SECRET or not API_TOKEN:
        return abort(500, "Required environment variables are not set.")

    # Get auth header and raw body
    auth_header = request.headers.get('Authorization')
    raw_body = request.get_data(as_text=True)

    # Validate the webhook signature
    signature = hmac.new(HOOK_SECRET.encode('utf-8'), raw_body.encode('utf-8'), hashlib.sha256).hexdigest()

    if signature != auth_header:
        return abort(403, "Signature mismatch. Unauthorized webhook.")

    full_body = json.loads(raw_body)
    hook_data = full_body['data']

    # Commands to skip logs
    commands_to_skip_logs = ['dbt source', 'dbt docs']

    # Extract run_id and account_id
    run_id = hook_data['runId']
    account_id = full_body['accountId']

    # Fetch run info from the dbt Cloud Admin API
    url = f'{DBT_API_URL}/accounts/{account_id}/runs/{run_id}/?include_related=["run_steps"]'
    headers = {'Authorization': f'Token {API_TOKEN}'}

    try:
        run_data_response = requests.get(url, headers=headers)
        run_data_response.raise_for_status()
    except requests.RequestException as e:
        return abort(500, f"Error fetching run data: {e}")

    run_data_results = run_data_response.json()['data']

    # Overall run summary
    status_emoji = "✅" if hook_data['runStatus'] == 'Success' else "❌"
    outcome_message = f"""
{status_emoji} *{hook_data['runStatus']} for Run #{run_id} on Job "{hook_data['jobName']}"*

*Environment:* {hook_data['environmentName']} | *Trigger:* {hook_data['runReason']} | *Duration:* {run_data_results['duration_humanized']}

*Run URL:* {run_data_results['href']}
"""

    # Step-specific summaries
    for step in run_data_results['run_steps']:
        if step['status_humanized'] == 'Success':
            outcome_message += f"\n✅ {step['name']} ({step['status_humanized']} in {step['duration_humanized']})"
        else:
            outcome_message += f"\n❌ {step['name']} ({step['status_humanized']} in {step['duration_humanized']})"
            show_logs = not any(cmd in step['name'] for cmd in commands_to_skip_logs)
            if show_logs:
                full_log = step['logs']
                full_log = re.sub(r'\x1b?\[[0-9]+m[0-9:]*', '', full_log)
                
                summary_start = re.search(r'(?:Completed with \d+ error.* and \d+ warnings?:|Database Error|Compilation Error|Runtime Error)', full_log)
                line_items = re.findall(r'(^.*(?:Failure|Error) in .*\n.*\n.*)', full_log, re.MULTILINE)

                if len(line_items) == 0:
                    relevant_log = f'```{full_log[summary_start.start() if summary_start else 0:]}```'
                else:
                    relevant_log = summary_start[0]
                    for item in line_items:
                        relevant_log += f'\n```\n{item.strip()}\n```\n'
                outcome_message += f"\n{relevant_log}"

    # Format the message for Google Chat
    payload = {
        "text": outcome_message
    }

    try:
        response = requests.post(GOOGLE_CHAT_WEBHOOK_URL, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error sending to Google Chat: {e}")
        return abort(500, f"Error sending to Google Chat: {e}")

    return jsonify({'outcome_message': outcome_message, 'webhook_status': 'Message sent successfully to Google Chat'}) 