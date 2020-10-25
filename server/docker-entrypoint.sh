#!/usr/bin/env bash
set -e

if [ "$1" = 'app' ]; then
    service nginx start
    cd ${APP_DIR}
    uwsgi --ini uwsgi.ini

    # chown -R postgres "$PGDATA"

    # if [ -z "$(ls -A "$PGDATA")" ]; then
    #     gosu postgres initdb
    # fi

    # exec gosu postgres "$@"
fi

exec "$@"
