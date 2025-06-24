#!/bin/bash

set -e 

if [ -f "manage.py" ]; then

    # env
    source /etc/django/django-env.sh
    source /etc/postgres/postgres-env.sh
    
    # migrations
    python "manage.py" makemigrations
    python "manage.py" migrate

    # superuser
    # python "manage.py" createsuperuser --noinput

    # collectstatic
    python "manage.py" collectstatic --noinput

    # runserver    
    gunicorn config.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 5 \
        --timeout 30 \
        --max-requests 1000 \
        --max-requests-jitter 100
        # --access-logfile /var/log/gunicorn/access.log \
        # --error-logfile /var/log/gunicorn/error.log

else
    echo "Django project not installed or incomplete — manage.py file missing"
    echo "Run django-admin startproject to create one"
    exec tail -f /dev/null
fi

exec "$@"
