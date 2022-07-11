from django.contrib import admin
from .models import Stages, Clients

# Register your models here.


@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'color', 'slug']

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'title', 'address', 'status_sales', 'status_competitors', 'additionally']
    fields = ['client_id', 'title', 'address', 'status_sales', 'status_competitors', 'additionally']


