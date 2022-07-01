from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='index'),
    path('books', views.books, name='booksList'),
    path('prestamos', views.prestamos, name='prestamos'),
    path('clientes/', views.users, name="clientes"),
    path('add-book', views.new_book, name="new_book"),
    path('new-user/', views.new_user, name="new_user"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)