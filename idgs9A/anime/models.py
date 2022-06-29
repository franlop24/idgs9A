from django.db import models

class Anime(models.Model):
    nombre_anime = models.CharField(max_length=100)  
    descripcion_anime = models.TextField()
    genero_anime = models.TextField()
    calificacion_anime = models.TextField()