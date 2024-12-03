web: gunicorn pettrust_backend.wsgi
worker: celery -A pettrust_backend worker --loglevel=info
beat: celery -A pettrust_backend beat --loglevel=info
