import os
from celery import Celery
from .settings import DEBUG

settings = 'src.development' if DEBUG else 'src.production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
