#!/usr/bin/env bash
python manage.py migrate
gunicorn pollapi.wsgi:application --bind 0.0.0.0:8000