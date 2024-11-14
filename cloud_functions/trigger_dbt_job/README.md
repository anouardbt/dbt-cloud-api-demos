# Trigger dbt Cloud Job with Google Cloud Function

This folder contains a Google Cloud Function that triggers a dbt Cloud job using the dbt Cloud API when invoked via an HTTP request.

## File Structure

- `main.py`: The main Python script that defines the Cloud Function.
- `requirements.txt`: Specifies dependencies required for the Cloud Function to run.
- `README.md`: Documentation for this function.

## Prerequisites

1. **Google Cloud Project**: Ensure you have a Google Cloud Project set up with permissions to deploy Cloud Functions.
2. **dbt Cloud Account**: A dbt Cloud account with API access.
3. **Environment Variables**: Set the following environment variables in your Cloud Function configuration:
   - `DBT_CLOUD_ACCOUNT_ID`: Your dbt Cloud account ID.
   - `DBT_CLOUD_API_TOKEN`: Your dbt Cloud API token.

## Deployment

1. Clone the repository:
   ```bash
   git clone https://github.com/anouardbt/dbt-cloud-api-demos.git
   cd dbt-cloud-api-demos/cloud_functions/trigger_dbt_job

```md
2. Deploy the Cloud Function using the Google Cloud CLI:

```bash
gcloud functions deploy trigger_dbt_job \
    --runtime python310 \
    --trigger-http \
    --allow-unauthenticated \
    --entry-point trigger_dbt_job
```

Make sure to replace `python310` with the appropriate version of Python if needed.

## Usage

To trigger the function, send an HTTP POST request with the following JSON payload:

```json
{
  "dbt_cloud_job_id": "YOUR_JOB_ID"
}
```

### Example cURL Request

```bash
curl -X POST https://YOUR_CLOUD_FUNCTION_URL \
-H "Content-Type: application/json" \
-d '{"dbt_cloud_job_id": "12345"}'
```

Replace `YOUR_CLOUD_FUNCTION_URL` with the deployed function URL and `12345` with the actual dbt Cloud job ID.
```