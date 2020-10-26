#!/usr/bin/env bash
set -e

if [ "$1" = 'app' ]; then
    cd ${APP_DIR}

    # if [ "${APP_}"]
    exec gosu www-data uwsgi --ini app.ini
fi

exec "$@"
