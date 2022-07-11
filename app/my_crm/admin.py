from django.contrib import admin
from .models import Stages

# Register your models here.


@admin.register(Stages)
class StagesAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'color']


