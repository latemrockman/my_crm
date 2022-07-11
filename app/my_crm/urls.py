from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('<slug:stage_slug>', views.index, name='index-stage'),
    path('client/', views.client, name='client-page'),
    path('settings/', views.settings, name='index-settings'),
    path('statistics/', views.statistics, name='index-statistics'),
]