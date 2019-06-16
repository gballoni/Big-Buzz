#!/bin/bash

echo "Rodando a versão de desenvolvimento..."
pip install --no-cache-dir -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

if [ ! -z "$1" ] && [ "$1" = "docker" ]; then
  python manage.py runserver_check 0.0.0.0:8000
else
  python manage.py runserver_check
fi
