
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'michael',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='ingestion_pipeline_demo',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['demo']
) as dag:

    validate_schema = BashOperator(
        task_id='validate_schema',
        bash_command='python ingestion/validate_schema.py --config ingestion/config.yml --table fct_sales'
    )

    load_to_warehouse = BashOperator(
        task_id='load_to_warehouse',
        bash_command='python ingestion/load_to_warehouse.py --file data/fct_sales.xlsx --table fct_sales'
    )

    validate_schema >> load_to_warehouse
