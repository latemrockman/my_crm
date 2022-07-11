from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('client/', views.client, name='client-page'),
    path('settings/', views.settings, name='settings-page'),
    path('statistics/', views.statistics, name='statistics-page'),
    path('calendar/', views.calendar, name='calendar-page'),
    path('<slug:stage_slug>/', views.stage, name='stage-page'),
]