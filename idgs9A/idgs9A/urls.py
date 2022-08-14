from django.conf import settings
from django.contrib import admin
from django.urls import path, include
#mport Directores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('peli/',include('Directores.urls')),
]