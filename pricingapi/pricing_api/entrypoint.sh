#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8003 # TODO to replace by a variable