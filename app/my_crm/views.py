from django.shortcuts import render
from .models import Stages

# Create your views here.


def index(request):
    return render(request, 'my_crm/index.html', {})

def stage(request, stage_slug):
    title_page = Stages.objects.get(slug=stage_slug).title
    return render(request, 'my_crm/index.html', {'title_page': title_page})

def client(request):
    return render(request, 'my_crm/client.html', {})

def settings(request):
    return render(request, 'my_crm/settings.html', {})

def statistics(request):
    return render(request, 'my_crm/statistics.html', {})
