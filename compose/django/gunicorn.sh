#!/bin/sh
python /app/manage.py collectstatic --noinput
# /usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5000 --chdir=/app
/usr/local/bin/gunicorn config.wsgi\
    -w 1\
    -b unix:/run/gunicorn/gunicorn.sock\
    --error-logfile /logs/gunicorn-errors.log\
    --access-logfile /logs/gunicorn-access.log\
    --chdir=/app
