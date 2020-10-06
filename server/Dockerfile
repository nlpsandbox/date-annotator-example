FROM python:3.8.5-slim-buster

ARG S6_VERSION
ENV S6_VERSION=${S6_VERSION:-v2.1.0.0}
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV PIP_NO_CACHE_DIR=off
ENV APP_USER=app
ENV APP_DIR=/opt/app

# Safer bash scripts with 'set -euxo pipefail'
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# Install dependencies
# hadolint ignore=DL3008
RUN apt-get update -qq -y \
    && apt-get install --no-install-recommends -qq -y \
        curl \
        unzip \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

# Set up S6 init system
RUN curl -fsSL https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz \
        -o /tmp/s6-overlay.tar.gz \
    && tar xzf /tmp/s6-overlay.tar.gz --directory / \
    && rm -fr /tmp/s6-overlay.tar.gz

# Add app user
RUN useradd -m -s /bin/bash ${APP_USER} \
    && echo "${APP_USER}:${APP_USER}" | chpasswd

# Copy server files
COPY . ${APP_DIR}
RUN chown -R ${APP_USER}:${APP_USER} ${APP_DIR}

# Install dependencies
RUN pip install -r ${APP_DIR}/requirements.txt

# Add s6 scripts
COPY root /

EXPOSE 8080

ENTRYPOINT ["/init"]
