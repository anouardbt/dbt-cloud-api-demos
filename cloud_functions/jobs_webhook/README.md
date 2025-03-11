# dbt Webhook Handler

## Overview
This script is a webhook handler for dbt Cloud, which verifies webhook signatures, fetches run details from dbt Cloud's API, processes the results, and sends formatted output to a specified webhook URL.

## Features
- Validates webhook signatures using HMAC and a shared secret.
- Fetches run details from dbt Cloud API.
- Filters logs for relevant error messages.
- Sends formatted results to a specified webhook.
- Configurable via environment variables.

## Environment Variables
The following environment variables must be set:

| Variable Name            | Description                                   |
|--------------------------|-----------------------------------------------|
| `DBT_WEBHOOK_KEY`       | Secret key for validating dbt webhook        |
| `DBT_CLOUD_SERVICE_TOKEN` | API token for accessing dbt Cloud API       |
| `DBT_API_URL`            | Base URL for dbt API (Default: `https://c1.us1.dbt.com/api/v2`) |
| `WEBHOOK_URL`           | URL to send the processed results            |

## Deployment Options
### Deploy as a Google Cloud Function
1. Enable Cloud Functions and Cloud Build in your GCP project.
2. Deploy the function using:
   ```sh
   gcloud functions deploy dbt_webhook_handler \
       --runtime python310 \
       --trigger-http \
       --allow-unauthenticated \
       --entry-point=http_function \
       --set-env-vars "DBT_WEBHOOK_KEY=<your_key>,DBT_CLOUD_SERVICE_TOKEN=<your_token>,WEBHOOK_URL=<your_webhook_url>"
   ```

### Deploy as an AWS Lambda Function
1. Create a Lambda function with Python runtime.
2. Set up API Gateway to trigger the function.
3. Upload the Python script as a Lambda function.
4. Configure environment variables in AWS Lambda console.

### Running Locally for Testing
1. Install dependencies:
   ```sh
   pip install flask requests
   ```
2. Set environment variables:
   ```sh
   export DBT_WEBHOOK_KEY=<your_key>
   export DBT_CLOUD_SERVICE_TOKEN=<your_token>
   export WEBHOOK_URL=<your_webhook_url>
   ```
3. Run the Flask app:
   ```sh
   flask run --host=0.0.0.0 --port=8080
   ```

## Usage
- Ensure the webhook is correctly set in dbt Cloud.
- The function will receive dbt Cloud webhooks, process them, and send structured logs to the configured `WEBHOOK_URL`.

## Contributing
Feel free to submit pull requests or open issues to improve this handler.

## License
This project is licensed under the MIT License.

