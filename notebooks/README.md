# Notebooks for dbt Cloud Integrations with GCP

This folder contains Jupyter Notebooks demonstrating various integrations between dbt Cloud and Google Cloud Platform (GCP) services. The notebooks showcase how to manage dbt Cloud jobs and export logs to GCP services such as Google Cloud Storage (GCS) and BigQuery.

## File Overview

### 1. `export_dbt_logs_to_gcs_bigquery.ipynb`
- **Description**: This notebook demonstrates how to fetch logs from dbt Cloud using its API and export these logs to Google Cloud Storage (GCS) and BigQuery for further analysis.
- **Key Features**:
  - Uses the dbt Cloud API to retrieve run logs and other artifacts.
  - Shows how to upload the retrieved logs to a GCS bucket.
  - Provides examples for ingesting and querying logs in BigQuery, enabling data analysis and monitoring.
- **Prerequisites**:
  - Access to a GCP project with GCS and BigQuery enabled.
  - A dbt Cloud account with API access.
  - Necessary permissions to interact with GCS and BigQuery.

### 2. `manage_dbt_jobs_rest_api.ipynb`
- **Description**: This notebook illustrates how to interact with the dbt Cloud REST API to manage jobs, including creating, triggering, monitoring, and retrieving job statuses.
- **Key Features**:
  - Demonstrates CRUD operations (Create, Read, Update, Delete) for dbt jobs using the API.
  - Automates workflows by integrating job operations within Python code, enabling complex data workflows.
  - Useful for orchestrating dbt Cloud jobs alongside GCP services or other automation tasks.
- **Prerequisites**:
  - A dbt Cloud account with API access.
  - A GCP project (optional, depending on use case).

## Getting Started

### Running the Notebooks

1. Clone the repository:
   ```bash
   git clone https://github.com/anouardbt/dbt-cloud-api-demos.git
   cd dbt-cloud-api-demos/notebooks
   ```
2. Open the notebooks using Jupyter Notebook, JupyterLab, or Google Colab:
   ```bash
   jupyter notebook
   ```
3. Follow the steps in each notebook to explore and execute the integrations.

### Required Libraries

Ensure you have the following Python libraries installed:

- `requests` (for making API calls)
- `google-cloud-storage` (for GCS interactions)
- `google-cloud-bigquery` (for BigQuery interactions)

To install these dependencies, run:

```bash
pip install requests google-cloud-storage google-cloud-bigquery
```

## License

This project is licensed under the MIT License.