from django.db import models

# Create your models here.
class Series(models.Model):
    serie_name = models.CharField(max_length=100)  
    serie_clasificacion = models.CharField(max_length=50)
    serie_num_capitulos = models.TextField()
    serie_num_temporadas = models.TextField()
    serie_poster = models.TextField()
    serie_ranking = models.TextField()
    serie_cast = models.TextField()
    # models.DateTimeField(auto_now_add=True) almacenara la fecha y hora del registro actual
    serie_created_at = models.DateTimeField(auto_now_add=True)
    serie_property_of = models.CharField(max_length=100)
    serie_trailer = models.TextField()
