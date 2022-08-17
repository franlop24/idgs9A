from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('peli/', views.peli, name='peli'),
    path('peli/', views.about, name='about'), 
]