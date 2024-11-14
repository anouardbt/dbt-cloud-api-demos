import requests
import os
import json

def trigger_dbt_job(request):
    """HTTP Cloud Function that triggers a dbt Cloud job with a specified job ID."""
    # Parse request JSON
    request_json = request.get_json(silent=True)
    
    if not request_json or 'dbt_cloud_job_id' not in request_json:
        return "Error: 'dbt_cloud_job_id' is required in the request body.", 400
    
    dbt_cloud_job_id = request_json['dbt_cloud_job_id']
    
    # Your dbt Cloud configuration
    dbt_cloud_account_id = os.environ.get('DBT_CLOUD_ACCOUNT_ID')  # set as an environment variable
    dbt_cloud_api_token = os.environ.get('DBT_CLOUD_API_TOKEN')  # set as an environment variable
    
    # dbt Cloud API endpoint
    url = f"https://cloud.getdbt.com/api/v2/accounts/{dbt_cloud_account_id}/jobs/{dbt_cloud_job_id}/run/"

    headers = {
        "Authorization": f"Token {dbt_cloud_api_token}",
        "Content-Type": "application/json"
    }

    # Optional: Add any parameters for the run, if needed
    payload = {
        "cause": "Triggered from Google Cloud Function"
    }

    # Make the request to trigger the dbt job
    response = requests.post(url, headers=headers, json=payload)

    # Handle the response
    if response.status_code == 200:
        return f"Successfully triggered dbt Cloud job with response: {response.json()}"
    else:
        return f"Failed to trigger dbt Cloud job. Status code: {response.status_code}, Response: {response.text}"