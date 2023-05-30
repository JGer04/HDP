from django.db import models

# Create your models here.

class Universidade(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    poblacion = models.IntegerField('poblacion', max_length=50)
    poblacion_discapacitados = models.IntegerField('poblacion_discapacitados' ,max_length=50)

    def __str__(self):
        return self.nombre