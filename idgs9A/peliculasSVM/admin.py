from django.contrib import admin
from .models import Peliculas
# Register your models here.
class PeliculasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Peliculas, PeliculasAdmin)

# Register your models here.
