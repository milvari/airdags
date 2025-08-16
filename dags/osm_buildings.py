#выгрузить из осма здания тбилиси и загрузить в базу данных
# -*- coding: utf-8 -*-

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.python import PythonOperator
import geopandas as gpd
import osmnx as ox
import sqlalchemy

#выгрузить из осма здания тбилиси
def osm_buildings_to_postgres():
    place = 'Tbilisi'
    tbilisi_buildings = ox.pois_from_place(place, tags={'building': True})

    # движок к базе данных
    db_url = 'postgresql://airflow:airflow@postgres:5432/airflow',
    engine = sqlalchemy.create_engine(db_url)

    # записать в базу данных
    gdf.to_postgis('tbilisi_buildings', engine, if_exists='replace', index=False, schema='public')

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
