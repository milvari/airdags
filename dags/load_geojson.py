from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import geopandas as gpd
import sqlalchemy

def load_geojson_to_postgres():
    # Path to the GeoJSON file
    geojson_path = '/opt/airflow/data/Event_shape_2025-07-28T14_56_57.633Z.geojson'
    # Read GeoJSON using GeoPandas
    gdf = gpd.read_file(geojson_path)

    # Database connection string from docker-compose
    db_url = 'postgresql://airflow:airflow@postgres:5432/airflow'
    engine = sqlalchemy.create_engine(db_url)

    # Write to PostgreSQL, table 'event', geometry column 'geom'
    gdf.to_postgis('event', engine, if_exists='replace', index=False, schema='public')

default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    'load_geojson_to_postgres',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    load_task = PythonOperator(
        task_id='load_geojson',
        python_callable=load_geojson_to_postgres
    )
