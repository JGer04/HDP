from django.shortcuts import render
from.models import *
# Create your views here.

def tablas(request):
    tActivos = Estudiantes_Activos_IES.objects.all().order_by('id')
    t2018 = Estudiantes_Genero_Tipo_2018.objects.all().order_by('id')
    t2019 = Estudiantes_Genero_Tipo_2019.objects.all().order_by('id')
    t2020 = Estudiantes_Genero_Tipo_2020.objects.all().order_by('id')
    tPrevalencia = Prevalencia_Estudiantes_Activos_IES.objects.all().order_by('id')

    return render(request, 'educacion/educacion.html',{
        'tActivos':tActivos,
        't2018':t2018,
        't2019':t2019,
        't2020':t2020,
        'tPrevalencia':tPrevalencia,
    })
