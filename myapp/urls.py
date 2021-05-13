from django.contrib import admin
from django.urls import path, include
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('team', views.team, name='team'),
]
