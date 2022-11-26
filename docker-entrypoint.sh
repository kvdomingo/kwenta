#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput || true

exec gunicorn --bind 0.0.0.0:$PORT --config gunicorn.conf.py --pid /tmp/gunicorn.pid
