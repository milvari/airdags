from kafka import KafkaProducer
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def send_kafka_message():
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    producer.send('airflow_test', b'Hello from Airflow')
    producer.close()

with DAG('kafka_test_dag', start_date=datetime(2025, 1, 1), schedule_interval=None, catchup=False) as dag:
    task = PythonOperator(
        task_id='send_kafka',
        python_callable=send_kafka_message
    )
