from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, timedelta
from airflow.utils.trigger_rule import TriggerRule
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
import boto3
import sys
import os
from src.trailer_extract import process_csv


api_key = os.getenv("TMDB_API_KEY")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_trailer_task():
    process_csv('/opt/airflow/src/dataset.csv','/opt/airflow/src/final_dataset.csv')


with DAG(
    'data_extraction',
    default_args=default_args,
    description='A consolidated dag for ETL',
    schedule=None,
    start_date=datetime(2024, 4, 21),
    catchup=False,
) as dag:
    
    extract_data_task= PythonOperator(
        task_id='extract_data_task',
        python_callable=extract_trailer_task,
    )
    


