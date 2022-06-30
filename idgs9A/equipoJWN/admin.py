from django.contrib import admin
from .models import Bar, Song, MagicTown

# Register your models here.
admin.site.register(Bar)
admin.site.register(Song)
admin.site.register(MagicTown)
