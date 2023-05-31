from django.db import models

# Create your models here.

class Universidad(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    poblacion = models.IntegerField('poblacion',)
    poblacion_discapacitados = models.IntegerField('poblacion_discapacitados',)
    class Meta:
        verbose_name_plural = "Universidad"

    def __str__(self):
        return self.nombre
    

