#from django.contrib.auth.models import User
from my_crm.models import Stages, Clients


def my_context(request):
    context = {
        'all_stages': Stages.objects.order_by('-id'),
        'all_clients': Clients.objects.order_by('-id'),
    }
    return context