from django.contrib import admin
from . models import Empresa, tablaNivel, tablaEncuestaRural, tablaEncuestaUrbana, tablaTipoDiscapacidad, tablaCategoria, resumen, analisis
# Register your models here.

admin.site.register(Empresa)
admin.site.register(tablaNivel)
admin.site.register(tablaEncuestaUrbana)
admin.site.register(tablaEncuestaRural)
admin.site.register(tablaTipoDiscapacidad)
admin.site.register(tablaCategoria)
admin.site.register(resumen)
admin.site.register(analisis)