#from django.contrib.auth.models import User
from my_crm.models import Stages, Clients


def my_context(request):
    all_stages = Stages.objects.order_by('-id')
    all_clients = Clients.objects.order_by('-id')

    compilation_new = Clients.objects.filter(stage_status=6)
    compilation_kp = Clients.objects.filter(stage_status=5)
    compilation_wait_requisites = Clients.objects.filter(stage_status=4)
    compilation_wait_contract = Clients.objects.filter(stage_status=3)
    compilation_finish = Clients.objects.filter(stage_status=2)
    compilation_cancel = Clients.objects.filter(stage_status=1)

    len_new = len(compilation_new)
    len_kp = len(compilation_kp)
    len_requisites = len(compilation_wait_requisites)
    len_contract = len(compilation_wait_contract)
    len_finish = len(compilation_finish)
    len_cancel = len(compilation_cancel)


    context = {
        'all_stages': all_stages,
        'all_clients': all_clients,
        'compilation_new': compilation_new,
        'compilation_kp': compilation_kp,
        'compilation_wait_requisites': compilation_wait_requisites,
        'compilation_wait_contract': compilation_wait_contract,
        'compilation_finish': compilation_finish,
        'compilation_cancel': compilation_cancel,
        'len_new': len_new,
        'len_kp': len_kp,
        'len_requisites': len_requisites,
        'len_contract': len_contract,
        'len_finish': len_finish,
        'len_cancel': len_cancel,

    }
    return context