from django.contrib import admin
from .models import Videogames
# Register your models here.
class VideogameAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Videogames, VideogameAdmin)
# Register your models here.
