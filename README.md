# dbt Cloud API Demos with GCP Integrations

Welcome to the **dbt-cloud-api-demos** repository! This repository showcases various ways to integrate dbt Cloud with the Google Cloud Platform (GCP) ecosystem using the dbt Cloud API. It includes examples that demonstrate triggering dbt jobs, exporting logs, and interacting with GCP services like Google Cloud Storage (GCS) and BigQuery.

## Repository Contents

### 1. `cloud_functions_trigger_dbt_cloud_job.py`
- **Description**: A Python script intended for use as a Google Cloud Function. It triggers a dbt Cloud job using the dbt Cloud API when invoked. The job ID can be passed dynamically as part of the request payload.
- **Key Features**:
  - Utilizes dbt Cloud's REST API to initiate jobs.
  - Configurable via environment variables for sensitive data like API tokens.
  - Suitable for event-driven workflows where dbt Cloud jobs are triggered based on GCP events.

### 2. `dbt_Cloud Logs to GCS and BigQuery.ipynb`
- **Description**: A Jupyter Notebook (created using Google Colab) demonstrating how to export and manage dbt Cloud logs by sending them to Google Cloud Storage (GCS) and ingesting them into BigQuery for further analysis and visualization.
- **Key Features**:
  - Fetches dbt Cloud logs using the dbt Cloud API.
  - Demonstrates uploading logs to GCS.
  - Provides examples of loading data into BigQuery tables for monitoring and analysis.

### 3. `jobs_rest_api.ipynb`
- **Description**: A Jupyter Notebook that illustrates interactions with dbt Cloud's REST API for managing jobs. It covers creating, triggering, and monitoring dbt jobs.
- **Key Features**:
  - Demonstrates various API operations (e.g., job creation, job runs, retrieving job statuses).
  - Automates dbt job workflows using GCP and the dbt Cloud API.
  - Useful for integrating dbt operations within GCP-based pipelines.

## Getting Started

### Prerequisites
- Python 3.x installed locally (for running scripts and notebooks).
- A dbt Cloud account with appropriate API access permissions.
- Access to a GCP project with roles and permissions to use Google Cloud Functions, BigQuery, and Cloud Storage.
- Jupyter Notebook or Google Colab for executing `.ipynb` files.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anouardbt/dbt-cloud-api-demos.git
   ```
2. Change to the repository directory:
   ```bash
   cd dbt-cloud-api-demos
   ```
3. Ensure all necessary Python dependencies are installed (e.g., `requests` for API calls).

### Usage

#### 1. Triggering a dbt Cloud Job with Google Cloud Functions
- Deploy the `cloud_functions_trigger_dbt_cloud_job.py` script as a Google Cloud Function.
- Set environment variables such as `DBT_CLOUD_ACCOUNT_ID` and `DBT_CLOUD_API_TOKEN`.
- Trigger the function via an HTTP request, including the job ID in the request payload.

#### 2. Exporting dbt Logs to GCS and BigQuery
- Open `dbt_Cloud Logs to GCS and BigQuery.ipynb` in Jupyter or Colab.
- Follow the steps to extract logs from dbt Cloud and push them to GCS and BigQuery.

#### 3. Managing dbt Jobs via the REST API
- Explore `jobs_rest_api.ipynb` to learn how to manage dbt jobs programmatically.
- Execute the cells to create, trigger, and monitor jobs using the dbt Cloud API.

## Contributing

Contributions are welcome! If you would like to contribute, please submit an issue or a pull request to help enhance the integrations and examples showcased in this repository.

## License

This repository is licensed under the [MIT License](LICENSE).
