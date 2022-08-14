from django.db import models

from django.db import models

class Pelicula(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre Pelicula")
    director = models.CharField(max_length=200, verbose_name="Director")
    sinopsi= models.TextField(verbose_name="Sinopsis")
    image=models.ImageField(verbose_name="Imagen",upload_to = "Pelicula")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Estreno")
    

    class Meta:
         verbose_name ="Pelicula"
         verbose_name_plural = "Peliculas"
         ordering = ['-created']

    def __str__(self):
         return self.title