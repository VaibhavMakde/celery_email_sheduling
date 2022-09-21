from django.http import HttpResponse
from django.shortcuts import render
from .tasks import *


# Create your views here.
def index(request):
    task1.delay()
    return HttpResponse("celery is working")
