#from django.contrib.auth.models import User
from my_crm.models import Stages, Clients


def my_context(request):

    context = {
        'all_stages': Stages.objects.order_by('-id'),
        'all_clients': Clients.objects.order_by('-id'),
        'compilation_new': Clients.objects.filter(stage_status=6),
        'compilation_kp': Clients.objects.filter(stage_status=5),
        'compilation_wait_requisites': Clients.objects.filter(stage_status=4),
        'compilation_wait_contract': Clients.objects.filter(stage_status=3),
        'compilation_finish': Clients.objects.filter(stage_status=2),
        'compilation_cancel': Clients.objects.filter(stage_status=1),
    }
    return context