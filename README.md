# dbt Cloud API Demos with GCP Integrations

This repository showcases various examples of integrating dbt Cloud with the Google Cloud Platform (GCP) ecosystem using the dbt Cloud API. The goal is to provide practical solutions and demonstrations of how dbt Cloud functionalities can be enhanced using GCP services such as Google Cloud Functions, Google Cloud Storage (GCS), BigQuery, and more.

## Repository Structure

### 1. `cloud_functions/`
Contains examples of Google Cloud Functions that interact with dbt Cloud:
- **`trigger_dbt_job/`**: A Cloud Function that triggers a dbt Cloud job using the dbt Cloud API when invoked. Useful for event-driven transformations and other automation scenarios.
- **`jobs_webhook/`**: A Cloud Function that listens for dbt Cloud webhook notifications, allowing automated responses or further actions based on job status updates. Ideal for real-time monitoring, alerting, or integration workflows.

### 2. `notebooks/`
Contains Jupyter Notebooks demonstrating integrations between dbt Cloud and GCP services:
- **`export_dbt_logs_to_gcs_bigquery.ipynb`**: Fetches logs from dbt Cloud using the API and exports them to GCS and BigQuery for further analysis.
- **`manage_dbt_jobs_rest_api.ipynb`**: Demonstrates how to manage dbt Cloud jobs using the REST API for creating, triggering, and monitoring job executions.

## Prerequisites

- A dbt Cloud account with API access.
- A Google Cloud Platform (GCP) project with necessary permissions for GCS, BigQuery, and Cloud Functions (as needed).
- Python 3.x with `requests` and relevant GCP libraries installed.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/anouardbt/dbt-cloud-api-demos.git
   cd dbt-cloud-api-demos
