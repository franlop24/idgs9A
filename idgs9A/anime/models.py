from statistics import mode
from django.db import models

class Anime(models.Model):
    nombre_anime = models.CharField(max_length=100)  
    descripcion_anime = models.TextField()
    genero_anime = models.TextField()
    imagen_anime = models.TextField()