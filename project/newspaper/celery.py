import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')

app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace='CELERY')



app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_post_week': {
        'task': 'news.tasks.send_week',
        'schedule': crontab(day_of_week='mondey', minute=0, hours = 8),
    },
}