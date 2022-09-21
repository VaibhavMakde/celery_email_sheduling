from celery import shared_task
from django.core.mail import send_mail
from celerytask import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta


# A task being bound means the
# first argument to the task will always be the task instance (self)
@shared_task(bind=True)
def task1(self):
    for i in range(10):
        print(i)
    return "Done"
