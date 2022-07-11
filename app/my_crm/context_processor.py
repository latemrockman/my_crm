#from django.contrib.auth.models import User
from my_crm.models import Stages


def my_context(request):
    context = {
        'all_stages': Stages.objects.all()
    }
    return context