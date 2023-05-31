from django.shortcuts import render
from.models import tablaEncuestaUrbana, tablaEncuestaRural, tablaTipoDiscapacidad, tablaCategoria, resumen, analisis
# Create your views here.

def tablas(request):
    tUrbano = tablaEncuestaUrbana.objects.all().order_by('id')
    tRural = tablaEncuestaRural.objects.all().order_by('id')
    tdiscapacidad = tablaTipoDiscapacidad.objects.all().order_by('id')
    tcategoria = tablaCategoria.objects.all().order_by('id')
    resumenn = resumen.objects.all().order_by('id')
    analisiss = analisis.objects.all().order_by('id')
    
    return render(request, 'trabajo/trabajo.html', {
        'tUrbano': tUrbano,
        'tRural': tRural,
        'tdiscapacidad': tdiscapacidad,
        'tcategoria':tcategoria,
        'resumen': resumenn,
        'analisis': analisiss
    })


