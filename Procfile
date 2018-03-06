web: gunicorn config.wsgi:application
worker: celery worker --app=message.taskapp --loglevel=info
