#!/bin/bash

find . -path “*/migrations/*.py” -not -name “__init__.py” -delete && 
find . -path “*/migrations/*.pyc” -delete && 
python manage.py makemigrations && 
python manage.py migrate && 
python manage.py shell < script.py && 
python manage.py loaddata whole.json && 
python manage.py runserver 0.0.0.0:8000 --insecure