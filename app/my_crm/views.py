from django.shortcuts import render
from .models import Stages

# Create your views here.


def index(request):
    stages = Stages.objects.all()
    return render(request, 'my_crm/index.html', {'stages': stages})

def stage(request, stage_slug):
    return render(request, 'my_crm/index.html', {})

def client(request):
    return render(request, 'my_crm/client.html', {})

def settings(request):
    return render(request, 'my_crm/settings.html', {})

def statistics(request):
    return render(request, 'my_crm/statistics.html', {})
