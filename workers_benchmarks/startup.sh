#!/usr/bin/env bash

until nc -z psql 5432; do
    echo "$(date) - waiting for postgres..."
    sleep 1
done


./manage.py migrate
exec /usr/local/bin/gunicorn workers_benchmarks.wsgi -c gunicorn-config.py
