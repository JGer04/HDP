from django.db import models

# Create your models here.

# --------- MODELO DE UNIVERSIDADES ----------------------
class Universidad(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    poblacion = models.IntegerField('poblacion',)
    poblacion_discapacitados = models.IntegerField('poblacion_discapacitados',)
    class Meta:
        verbose_name_plural = "Universidad"

    def __str__(self):
        return self.nombre

# --------- MODELO RESUMEN ----------------------
class resumen(models.Model):
    resumen = models.TextField()
    class Meta:
        verbose_name_plural = "Resumen"

# --------- MODELO ANÁLISIS ----------------------
class analisis(models.Model):
    analisis = models.TextField(default='')
    class Meta:
        verbose_name_plural = "Análisis"
 
# --------- MODELO DE TABLA ESTUDIANTES ACTIVOS ----------------------
class Estudiantes_Activos_IES(models.Model):
    año = models.IntegerField()
    fisica = models.IntegerField()
    intelectual = models.IntegerField()
    sensorial = models.IntegerField()
    mental = models.IntegerField()
    total = models.IntegerField()
    class Meta:
        verbose_name_plural = "Estudiantes activos IES 2018-2020"
    
    def __str__(self):
        return str(self.año) + str(self.total)

# --------- MODELO DE TABLA DE ESTUDIANTES-GENERO-TIPO (2018) ----------------------    
class Estudiantes_Genero_Tipo_2018(models.Model):
    discapacidad = models.CharField('discapacidad', max_length=50)
    masculino = models.IntegerField()
    femenino = models.IntegerField()
    class Meta:
        verbose_name_plural = "Estudiantes por Genero y Discapacidad (2018)"

    def __str__(self):
        return self.discapacidad + str(self.masculino) + str(self.femenino)

# --------- MODELO DE TABLA DE ESTUDIANTES-GENERO-TIPO (2019) ----------------------
class Estudiantes_Genero_Tipo_2019(models.Model):
    discapacidad = models.CharField('discapacidad', max_length=50)
    masculino = models.IntegerField()
    femenino = models.IntegerField()
    class Meta:
        verbose_name_plural = "Estudiantes por Genero y Discapacidad (2019)"

    def __str__(self):
        return self.discapacidad + str(self.masculino) + str(self.femenino)

# --------- MODELO DE TABLA DE ESTUDIANTES-GENERO-TIPO (2020) ----------------------
class Estudiantes_Genero_Tipo_2020(models.Model):
    discapacidad = models.CharField('discapacidad', max_length=50)
    masculino = models.IntegerField()
    femenino = models.IntegerField()
    class Meta:
        verbose_name_plural = "Estudiantes por Genero y Discapacidad (2020)"

    def __str__(self):
        return self.discapacidad + str(self.masculino) + str(self.femenino)
 
# --------- MODELO DE TABLA DE PREVALENCIA DE DISCAPACIDADES ----------------------
class Prevalencia_Estudiantes_Activos_IES(models.Model):
    discapacidad = models.CharField('discapacidad', max_length=50)
    año_2018 = models.IntegerField()
    año_2019 = models.IntegerField()
    año_2020 = models.IntegerField()
    total = models.IntegerField()
    porcentaje = models.CharField('porcentaje',max_length=50)
    class Meta:
        verbose_name_plural = "Prevalencia de Discapacidad (2018-2020)"

    def __str__(self):
        return self.discapacidad + str(self.total)

    

