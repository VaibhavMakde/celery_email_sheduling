from django.http import HttpResponse
from django.shortcuts import render
from django_celery_beat.models import CrontabSchedule, PeriodicTask
# from .tasks import send_mail_func
from app.tasks import task1
from send_mail_app.tasks import send_mail_func


# Create your views here.
def test(request):
    task1.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=17, minute=45)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" + "1",
                                       task='send_mail_app.tasks.send_mail_func')  # , args = json.dumps([[2,3]]))
    return HttpResponse("Done")
