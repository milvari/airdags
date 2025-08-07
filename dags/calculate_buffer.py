from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="calculate_buffer",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    create_table = PostgresOperator(
        task_id="calculate_buffer",
        postgres_conn_id="postgres_default",
        sql="""
        DROP TABLE IF EXISTS event_buffer;
        CREATE TABLE IF NOT EXISTS event_buffer AS
        SELECT polygonlabel, ST_Buffer(geometry::geography, 500000) FROM event;
        """,
    )