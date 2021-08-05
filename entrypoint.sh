#! /bin/sh

python manage.py makemigrations --no-input

python manage.py migrate --no-input

exec qunicorn debt.wsgi:application -b 0.0.0.0:8000 --reload