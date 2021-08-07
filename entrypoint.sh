#!/bin/sh

python manage.py migrate

gunicorn debt.wsgi:application --bind 0.0.0.0:8000 --reload -w 4