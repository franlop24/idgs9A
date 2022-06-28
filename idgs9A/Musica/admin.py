from django.contrib import admin
from .models import Musica

class MusicaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Musica, MusicaAdmin)

# Register your models here.
