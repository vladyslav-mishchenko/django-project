#!/bin/bash

set -e 

if [ -f "manage.py" ]; then

    # migrations
    python "manage.py" makemigrations
    python "manage.py" migrate

    # superuser
    # python "manage.py" createsuperuser --noinput

    # collectstatic
    # python "manage.py" collectstatic --noinput

    # Load data
    python manage.py load_pages_data || echo "Failed to load pages data"
    python manage.py load_main_menu_data || echo "Failed to load menu data"
    python manage.py load_blog_data || echo "Failed to load blog data"

    # runserver
    python "manage.py" runserver 0.0.0.0:8000

else
    echo "Django project not installed or incomplete — manage.py file missing"
    echo "Run django-admin startproject to create one"
    exec tail -f /dev/null
fi

exec "$@"
