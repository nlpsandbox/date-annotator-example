FROM python:3.8.5-slim-buster

ENV PIP_NO_CACHE_DIR=off
ENV APP_USER=app
ENV APP_DIR=/opt/app

# Safer bash scripts with 'set -euxo pipefail'
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# TODO: Try comment out packages to see what is needed
# Install dependencies
# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        build-essential \
        python3-dev \
        nginx  \
        # uWSGI with pcre support
        libpcre3 \
        libpcre3-dev \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

# Add app user
RUN useradd -m -s /bin/bash ${APP_USER} \
    && echo "${APP_USER}:${APP_USER}" | chpasswd

# Copy server files
COPY openapi_server ${APP_DIR}/openapi_server
COPY requirements.txt uwsgi.ini ${APP_DIR}/
COPY nginx.conf /etc/nginx
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

# RUN chown -R ${APP_USER}:${APP_USER} ${APP_DIR}

# Install dependencies
RUN pip install -r ${APP_DIR}/requirements.txt



EXPOSE 8080

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["app"]