FROM postgis/postgis:16-3.4-alpine
USER root

# runtime + build deps (для сборки pg_h3 нужны cmake и заголовки PG)
RUN apk add --no-cache \
      ca-certificates curl \
      python3 py3-pip \
      libstdc++ \
  && apk add --no-cache --virtual .build-deps \
      build-base git cmake \
      postgresql16-dev

# venv для pgxnclient → сборка и установка h3, затем уборка
RUN python3 -m venv /opt/pgxn \
  && . /opt/pgxn/bin/activate \
  && pip install --no-cache-dir pgxnclient \
  && /opt/pgxn/bin/pgxn install h3 \
  && rm -rf /opt/pgxn \
  && apk del .build-deps \
  && rm -rf /root/.cache /var/cache/apk/*

COPY create_h3.sql /docker-entrypoint-initdb.d/

USER postgres
