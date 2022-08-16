from django.db import models
from django.forms import model_to_dict

from django.db import models

# Create your models here.

class Libro(models.Model):
    Nombre = models.CharField(max_length=50)
    Autor = models.CharField(max_length=65)
    fecha_de_publicasion = models.DateField()
    ID_libro = models.DateField()

class Usuario(models.Model):
    Nombre = models.CharField(max_length=25)
    ApellidoP = models.CharField(max_length=50)
    ApellidoM = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Numero_de_usuario = models.IntegerField()

class Estantes(models.Model):
    Tipo_de_obras = models.CharField(max_length=25)
    Alfabetisacion =models.CharField(max_length=45)

class Debolucion_de_libro(models.Model):
    Hora = models.IntegerField()
    Fecha = models.IntegerField()
    Numero_de_Usuario =models.IntegerField()

class Obtension_de_libro(models.Model):
    Hora = models.IntegerField()
    Fecha = models.IntegerField()
    Numero_de_Usuario =models.IntegerField()

class Bibliotecario(models.Model):
    Nombre = models.CharField(max_length=25)
    ApellidoP = models.CharField(max_length=50)
    ApellidoM = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Numero_de_usuario = models.IntegerField()

class Empleados(models.Model):
    Nombre = models.CharField(max_length=25)
    ApellidoP = models.CharField(max_length=50)
    ApellidoM = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Numero_de_empleado = models.IntegerField()
    Seccion_de_trabajo = models.CharField(max_length=65)

