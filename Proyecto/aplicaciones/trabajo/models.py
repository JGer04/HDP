from django.db import models

# Create your models here.

# --------- MODELO DE EMPRESAS ----------------------
class Empresa(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    total_trabajadores = models.IntegerField('total_trabajadores',)
    trabajadores_discapacitados = models.IntegerField('trabajadores_discapacitados',)
    class Meta:
        verbose_name_plural = "Empresa"
    
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

# --------- MODELO DE LA TABLA NIVELES ----------------------
class tablaNivel(models.Model):
    nivel = models.CharField(max_length=50)
    total = models.IntegerField()
    hombre = models.IntegerField()
    mujer = models.IntegerField()
    class Meta:
        verbose_name_plural = "tabla Nivel"

    def __str__(self):
        return self.nivel

# --------- MODELO DE LA ENCUESTA EN ZONA URBANA ----------------------
class tablaEncuestaUrbana(models.Model):
    grupoEdad = models.CharField(max_length=50)
    total = models.IntegerField()
    hombre = models.IntegerField()
    mujer = models.IntegerField()
    class Meta:
        verbose_name_plural = "Encuesta Urbana"

    def __str__(self):
        return str(self.total)

# --------- MODELO DE LA ENCUESTA EN ZONA RURAL ----------------------
class tablaEncuestaRural(models.Model):
    grupoEdad = models.CharField(max_length=50)
    total = models.IntegerField()
    hombre = models.IntegerField()
    mujer = models.IntegerField()
    class Meta:
        verbose_name_plural = "Encuesta Rural"
    
    def __str__(self):
        return str(self.total)
    
# --------- MODELO DE LA TABLA CATEGORÍA ----------------------
class tablaCategoria(models.Model):
    categoria = models.CharField(max_length=50)
    hombre = models.IntegerField()
    mujer = models.IntegerField()
    total = models.IntegerField()
    class Meta:
        verbose_name_plural = "Tabla Categoria"
    
    def __str__(self):
        return str(self.categoria)

# --------- MODELO DE LA TABLA DE TIPO DE DISCAPACIDAD ----------------------
class tablaTipoDiscapacidad(models.Model):
    discapacidad = models.CharField(max_length=50, default='')
    numero_Ocupadas = models.IntegerField(default=0)
    porcentaje_Ocupadas = models.CharField(max_length=50, default='')
    numero_Desocupadas = models.IntegerField(default=0)
    porcentaje_Desocupadas = models.CharField(max_length=50, default='')
    numero_Inactivas = models.IntegerField(default=0)
    porcentaje_Inactivas = models.CharField(max_length=50, default='')
    class Meta:
        verbose_name_plural = "Tabla Tipo Discapacidad"
    
    def __str__(self):
        return self.discapacidad

    