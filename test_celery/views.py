from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from test_celery.tasks import test_celery


def index(request):
    port = request.get_port()
    
    return HttpResponse(f"Hello, world. You're at the polls index. You're using port: {port}.")
