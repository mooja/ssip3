#!/bin/sh

docker-compose -f docker-compose-dev.yml run django python manage.py $@
