# from django.contrib import admin
from django.conf import settings
from django.urls import path
from numbers import Integral
from . import views


urlpatterns = [
    # path('admin', admin.site.urls),
    path('', views.home, name='home'),
    path('bares', views.bars, name="bars"),
    path('musica', views.songs, name="songs"),
    path('pueblos-magicos', views.towns, name="towns"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)