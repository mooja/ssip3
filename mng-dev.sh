#!/bin/sh

docker-compose -f docker-compese-dev.yml run django python manage.py $@
