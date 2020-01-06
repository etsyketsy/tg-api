#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
exec /opt/miniconda/envs/tg-info/bin/uwsgi --ini /scripts/uwsgi.ini
