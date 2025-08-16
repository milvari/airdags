FROM apache/airflow:2.9.1-python3.9

USER root
RUN apt-get update && apt-get install -y libspatialindex-dev gdal-bin libgdal-dev
USER airflow

RUN pip install geopandas psycopg2-binary sqlalchemy geoalchemy2 osmnx
RUN pip install --upgrade osmnx
RUN pip install redis 'flask-limiter[redis]'
RUN pip install kafka-python
