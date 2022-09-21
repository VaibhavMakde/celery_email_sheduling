from celery import shared_task
from django.core.mail import send_mail
from celerytask import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    print(users)
    print(settings.EMAIL_HOST_USER)
    # timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        to_email = user.email
        print(
            mail_subject,
            message,
        )
        print('FROM ID :', settings.EMAIL_HOST_USER)
        print('recipient :', to_email)
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=True,
        )
    return "Done"
