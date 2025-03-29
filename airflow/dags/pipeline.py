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
        description='ETL pipeline',
        schedule_interval='@daily',
        start_date=datetime(2025, 3, 28),
        catchup=False,
        default_args=default_args,
) as dag:
    migration_bronze_level = BashOperator(
        task_id='migration_bronze_level',
        bash_command='cd /opt/airflow/bronze_level && pyway migrate'
    )

    bronze_level = BashOperator(
        task_id='bronze_level',
        bash_command='python3 /opt/airflow/bronze_level/main.py'
    )

    migration_silver_level = BashOperator(
        task_id='migration_silver_level',
        bash_command='cd /opt/airflow/silver_level && pyway migrate'
    )

    silver_level = BashOperator(
        task_id='silver_level',
        bash_command='python3 /opt/airflow/silver_level/main.py'
    )

    migration_bronze_level >> bronze_level >> migration_silver_level >> silver_level
