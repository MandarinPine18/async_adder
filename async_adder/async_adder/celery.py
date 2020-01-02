import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_adder.settings')

celery_app = Celery('async_adder')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
