#!/bin/bash

python manage.py loaddata whole.json &&  python manage.py runserver 0.0.0.0:8000