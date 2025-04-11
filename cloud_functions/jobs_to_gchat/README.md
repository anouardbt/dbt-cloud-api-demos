# dbt Cloud to Google Chat Webhook

This Cloud Function receives webhooks from dbt Cloud and forwards them to a Google Chat space. It provides detailed information about dbt Cloud job runs, including success/failure status, duration, and error logs.

## Setup

1. Deploy this function to your preferred cloud provider (Google Cloud Functions, AWS Lambda, etc.)

2. Set the following environment variables:
   - `DBT_WEBHOOK_KEY`: The webhook secret from dbt Cloud
   - `DBT_CLOUD_SERVICE_TOKEN`: Your dbt Cloud service token
   - `DBT_API_URL`: (Optional) The dbt Cloud API URL (defaults to https://c1.us1.dbt.com/api/v2)
   - `GOOGLE_CHAT_WEBHOOK_URL`: (Optional) The Google Chat webhook URL (defaults to the provided URL)

3. Configure the webhook in dbt Cloud:
   - Go to Account Settings > Webhooks
   - Add a new webhook
   - Set the URL to your deployed function's URL
   - Set the Secret to match your `DBT_WEBHOOK_KEY`
   - Select the events you want to receive notifications for

## Message Format

The function sends formatted messages to Google Chat with the following information:
- Job run status (Success/Failure)
- Job name and run ID
- Environment and trigger information
- Duration
- Run URL
- Step-by-step execution details
- Error logs (if any)

## Local Testing

To test locally:
1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables
3. Use a tool like ngrok to expose your local server
4. Update the webhook URL in dbt Cloud to point to your ngrok URL

## Security

- The function validates webhook signatures using the provided secret
- All sensitive information is stored as environment variables
- The function uses HTTPS for all API calls 