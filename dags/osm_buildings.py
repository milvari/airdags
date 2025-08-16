#выгрузить из осма здания тбилиси и загрузить в базу данных
# пересчитать в гексагоны 

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
import geopandas as gpd
import osmnx as ox
import sqlalchemy

#выгрузить из осма здания тбилиси
def osm_buildings_to_postgres():
    place = 'Tbilisi'
    tbilisi_buildings = ox.features_from_place(place, tags={'building': True})

    # движок к базе данных
    db_url = 'postgresql://airflow:airflow@postgres:5432/airflow'
    engine = sqlalchemy.create_engine(db_url)

    # записать в базу данных
    tbilisi_buildings.to_postgis('tbilisi_buildings', engine, if_exists='replace', index=False, schema='public')


default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    'osm_buildings_to_postgres',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    load_task = PythonOperator(
        task_id='osm_buildings_to_postgres',
        python_callable=osm_buildings_to_postgres
    )

    create_table = PostgresOperator(
        task_id="buildings_to_h3",
        postgres_conn_id="postgres_default",
        sql="buildings_to_h3.sql"
    )

    load_task >> create_table