from numbers import Integral
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='index'),
    path('animes', views.listaAnimes, name='animes'),
    path('registrar-anime/', views.registrar_anime, name="registrar_anime"),
    path('eliminar-anime/<int:id>', views.borrar_anime)
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)