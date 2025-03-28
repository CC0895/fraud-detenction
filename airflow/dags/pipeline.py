from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Definiamo il DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'pipeline',
    description='etl',
    schedule_interval='@daily',  #
    start_date=datetime(2025, 3, 28),
    catchup=False,
    default_args=default_args,
) as dag:

    # Definiamo l'operatore per eseguire lo script
    bronze_level = BashOperator(
        task_id='bronze_level',
        bash_command='python3 bronze_level/main.py'
    )
    silver_level = BashOperator(
        task_id='silver_level',
        bash_command='python3 silver_level/main.py'
    )

    bronze_level >> silver_level
