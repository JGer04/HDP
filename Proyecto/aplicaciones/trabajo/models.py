from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    total_trabajadores = models.IntegerField('total_trabajadores',)
    trabajadores_discapacitados = models.IntegerField('trabajadores_discapacitados',)
    
    def __str__(self):
        return self.nombre
    