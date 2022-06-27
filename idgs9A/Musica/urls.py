from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('inicio/', views.inicio, name="inicio"),
    path('cancion/', views.cancion, name="cancion"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]
