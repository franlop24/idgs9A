from django.contrib import admin
from .models import Videogame
# Register your models here.
class VideogameAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Videogame, VideogameAdmin)
# Register your models here.
