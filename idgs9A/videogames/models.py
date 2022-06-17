from django.db import models

# Create your models here.


class Videogame(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo del Videojuego")
    subtitle = models.CharField(max_length=200, verbose_name="Plataforma")
    content= models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Imagen",upload_to = "videogames")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta:
         verbose_name ="videogames"
         verbose_name_plural = "videogames"
         ordering = ['-created']

    def __str__(self):
         return self.title