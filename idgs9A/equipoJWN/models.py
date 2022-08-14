from django.db import models

# Create your models here.
class Bar(models.Model):
    title    = models.CharField(max_length=50, verbose_name="Título")
    barKind  = models.CharField(max_length=50, verbose_name="Tipo de bar")
    location = models.TextField(verbose_name="Ubicacion")
    menu     = models.TextField()
    image    = models.ImageField(upload_to="bars", verbose_name="Imagen")

    class Meta:
        verbose_name = "bar"
        verbose_name_plural = "barres"
        ordering = ["-title"]
    
    def __str__(self):
        return self.title


class MagicTown(models.Model):
    title         = models.CharField(max_length=100, verbose_name="Título")
    state         = models.CharField(max_length=50, verbose_name="Estado")
    description   = models.TextField(verbose_name="Descripción")
    accommodation = models.BooleanField(verbose_name="Hospedaje")
    culturalZones = models.BooleanField(verbose_name="Zonas culturales")
    image         = models.ImageField(upload_to="towns", verbose_name="Imagen")

    class Meta:
        verbose_name = "pueblo magico"
        verbose_name_plural = "pueblos magicos"
        ordering = ["-title"]

    def __str__(self):
        return self.title