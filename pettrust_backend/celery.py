from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pettrust_backend.settings')

app = Celery('pettrust_backend')

# Using the Django settings for Celery configuration
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Optionally, configure retry behavior for the broker connection
app.conf.broker_connection_retry_on_startup = True
