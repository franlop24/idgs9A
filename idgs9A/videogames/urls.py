from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('about', views.about, name='about'),
    path('detail', views.gameDetail, name='detail'),
]