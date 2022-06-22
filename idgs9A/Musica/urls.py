from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.home, name="home"),
    path('cancion/', views.cancion, name="cancion"),
    path('album/', views.album, name="album"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
    path('admin/', admin.site.urls),
]