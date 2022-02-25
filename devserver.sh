#!/bin/sh

screen -d -m -S fangorn-backend poetry run python manage.py runserver 0.0.0.0:8000 
