from django.shortcuts import render
from.models import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def tablas(request):
    tUrbano = tablaEncuestaUrbana.objects.all().order_by('id')
    tRural = tablaEncuestaRural.objects.all().order_by('id')
    tdiscapacidad = tablaTipoDiscapacidad.objects.all().order_by('id')
    tcategoria = tablaCategoria.objects.all().order_by('id')
    resumenn = resumen.objects.all().order_by('id')
    analisiss = analisis.objects.all().order_by('id')
    tnivel = tablaNivel.objects.all().order_by('id')
    
    return render(request, 'trabajo/trabajo.html', {
        'tUrbano': tUrbano,
        'tRural': tRural,
        'tdiscapacidad': tdiscapacidad,
        'tcategoria':tcategoria,
        'resumen': resumenn,
        'analisis': analisiss,
        'tnivel':tnivel,
    })

class crearTabla(CreateView):
    template_name = 'trabajo/modificar.html'
    model = tablaNivel
    fields = ['nivel','total','hombre','mujer']
    success_url = reverse_lazy('trabajo/trabajo.html')

