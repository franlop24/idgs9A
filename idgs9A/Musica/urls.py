from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('album/', views.album, name="album"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="aboutus"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
    path('admin/', admin.site.urls),
]