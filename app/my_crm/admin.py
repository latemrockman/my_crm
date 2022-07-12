from django.contrib import admin
from .models import Stages, Clients, MatStatus

# Register your models here.


@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'color']

@admin.register(MatStatus)
class MatStatusAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title']


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['title', 'address', 'stage_status', 'mat_status', 'additionally']
    fields = ['title', 'address', 'stage_status', 'mat_status', 'additionally']


