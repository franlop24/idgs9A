from numbers import Integral
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='index'),
    path('series', views.seriesList, name='seriesList'),
    path('detail', views.seriesList, name='detail'),
    #path('ejemplo/', views.ejemplo, name="ejemplo"),
    path('crear-serie-url/<str:serie_name>/<str:serie_clasificacion>/<str:serie_num_capitulos>/<str:serie_num_temporadas>/<str:serie_poster>/<str:serie_ranking>', views.crear_series_url, name="crear_series_url"),
    #path('serie/', views.serie, name="serie"),
    #path('actualizar-serie/<int:id>', views.actualizar_Serie, name="actualizar_Serie"),
    #path('serie-found/<int:id>', views.Serie_Found, name="serie_found"),
    #path('crear-serie/', views.crear_series, name="crear_series"),
    #path('delete_serie/<int:id>', views.delete_serie, name="delete_serie"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)