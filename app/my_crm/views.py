from django.shortcuts import render
from .models import Stages, Clients

# Create your views here.


def index(request):
    #for client in Clients.objects.all():
    #    client.save()
    return render(request, 'my_crm/index.html', {})

def stage(request, stage_slug):
    title_page = Stages.objects.get(slug=stage_slug).title
    ss = Stages.objects.get(title=title_page)

    compilation = Clients.objects.filter(stage_status=ss)

    context = {
        'title_page': title_page,
        'compilation': compilation,
        'ss': ss
    }

    return render(request, 'my_crm/index.html', context)

def client(request, client_slug):
    client =Clients.objects.get(slug=client_slug)
    title = Clients.objects.get(slug=client_slug).title
    return render(request, 'my_crm/client.html', {'client': client})

def settings(request):
    return render(request, 'my_crm/settings.html', {})

def statistics(request):
    return render(request, 'my_crm/statistics.html', {})

def calendar(request):
    return render(request, 'my_crm/calendar.html', {})