#!/bin/bash

echo "Rodando a versão de desenvolvimento..."
sudo pip install --no-cache-dir -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver_check 0.0.0.0:8000
