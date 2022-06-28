from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('inicio/', views.inicio, name="inicio"),
    path('cancion/', views.cancion, name="cancion"),
    path('album/', views.album, name="album"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

#Config Musica
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root
    =settings.MEDIA_ROOT)

