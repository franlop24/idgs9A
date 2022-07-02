from numbers import Integral
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='index_videogames'),
    path('about', views.about, name='about_videogames'),
    path('detail', views.gameDetail, name='detail_videogames'),
    path('games', views.games, name='games'),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)