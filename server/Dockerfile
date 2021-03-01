FROM python:3.9.2-slim-buster

ENV APP_DIR=/opt/app

SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        build-essential \
        gosu \
        libpcre3 \
        libpcre3-dev \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

COPY openapi_server ${APP_DIR}/openapi_server
COPY requirements.txt uwsgi.ini ${APP_DIR}/
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

RUN pip install --no-cache-dir \
    -r ${APP_DIR}/requirements.txt uWSGI==2.0.19.1

EXPOSE 8080

ENTRYPOINT ["/docker-entrypoint.sh"]

# Run server in development mode
# CMD ["python", "-m", "openapi_server"]

# Run server in production mode
CMD ["uwsgi", "--ini", "uwsgi.ini", "--lazy", "--http", ":8080"]