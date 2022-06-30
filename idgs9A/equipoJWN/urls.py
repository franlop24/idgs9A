from django.contrib import admin
from django.urls import path
from core import views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bares/', views.bars, name="bars"),
    path('musica/', views.music, name="music"),
    path('pueblos-magicos/', views.towns, name="towns"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)