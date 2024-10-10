from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from test_celery.tasks import test_celery


def index(request):
    task = test_celery.delay()
    return HttpResponse("Hello, world. You're at the polls index.")
