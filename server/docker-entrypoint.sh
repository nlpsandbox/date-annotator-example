#!/usr/bin/env bash
set -e

if [ "$1" = 'app' ]; then
    cd ${APP_DIR}
    exec gosu "${APP_UID}" uwsgi --ini app.ini
fi

exec "$@"
