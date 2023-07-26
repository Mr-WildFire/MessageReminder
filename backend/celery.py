import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    CELERYBEAT_SCHEDULE={
        # "every_10_seconds": {
        #     'task': "email_alert.tasks.print_hello",
        #     'schedule': timedelta(seconds=10),
        # },
        "every_day_20_or_22_hour": {
            'task': "email_alert.tasks.send_email",
            'schedule': crontab(minute=46, hour="9")
        }
    }
)
