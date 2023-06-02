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
# -------------------- CRUD DE TABLA NIVELES ------------------------------
class crearTablaN(CreateView):
    template_name = 'trabajo/tabla-nivel/crear.html'
    model = tablaNivel
    fields = ['nivel','total','hombre','mujer']
    success_url = reverse_lazy('trabajo_app:trabajo')

class modificarTablaN(UpdateView):
    template_name = 'trabajo/tabla-nivel/modificar.html'
    model = tablaNivel
    fields = ['nivel','total','hombre','mujer']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('trabajo')

class eliminarTablaN(DeleteView):
    template_name = 'trabajo/tabla-nivel/eliminar.html'
    model = tablaNivel
    fields = ['nivel','total','hombre','mujer']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('trabajo')

# -------------------- CRUD DE TABLA ENC. URBANA ---------------------------

class crearTablaUR(CreateView):
    template_name = 'trabajo/encuesta-urbana/crear.html'
    model = tablaEncuestaUrbana
    fields = ['grupoEdad','total','hombre','mujer']
    success_url = reverse_lazy('trabajo')

class modificarTablaUR(UpdateView):
    template_name = 'trabajo/encuesta-urbana/modificar.html'
    model = tablaEncuestaUrbana
    fields = ['grupoEdad','total','hombre','mujer']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('trabajo')

class eliminarTablaUR(DeleteView):
    template_name = 'trabajo/encuesta-urbana/eliminar.html'
    model = tablaEncuestaUrbana
    fields = ['grupoEdad','total','hombre','mujer']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('trabajo')

# -------------------- CRUD DE TABLA ENC. RURAL ---------------------------

class crearTablaRU(CreateView):
    template_name = 'trabajo/encuesta-rural/crear.html'
    model = tablaEncuestaRural
    fields = ['grupoEdad','total','hombre','mujer']
    success_url = reverse_lazy('trabajo')

class modificarTablaRU(UpdateView):
    template_name = 'trabajo/encuesta-rural/modificar.html'
    model = tablaEncuestaRural
    fields = ['grupoEdad','total','hombre','mujer']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('trabajo')

class eliminarTablaRU(DeleteView):
    template_name = 'trabajo/encuesta-rural/eliminar.html'
    model = tablaEncuestaRural
    fields = ['grupoEdad','total','hombre','mujer']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('trabajo')

# -------------------- CRUD DE TABLA TIPO DISCAPACIDAD ---------------------------

class crearTablaDI(CreateView):
    template_name = 'trabajo/tipo-disc/crear.html'
    model = tablaTipoDiscapacidad
    fields = ['discapacidad','numero_Ocupadas','porcentaje_Ocupadas','numero_Desocupadas','porcentaje_Desocupadas','numero_Inactivas','porcentaje_Inactivas']
    success_url = reverse_lazy('trabajo')

class modificarTablaDI(UpdateView):
    template_name = 'trabajo/tipo-disc/crear.html'
    model = tablaTipoDiscapacidad
    fields = ['discapacidad','numero_Ocupadas','porcentaje_Ocupadas','numero_Desocupadas','porcentaje_Desocupadas','numero_Inactivas','porcentaje_Inactivas']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('trabajo')

class eliminarTablaDI(DeleteView):
    template_name = 'trabajo/tipo-disc/crear.html'
    model = tablaTipoDiscapacidad
    fields = ['discapacidad','numero_Ocupadas','porcentaje_Ocupadas','numero_Desocupadas','porcentaje_Desocupadas','numero_Inactivas','porcentaje_Inactivas']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('trabajo')

# -------------------- CRUD DE TABLA CATEGORIA ---------------------------

class crearTablaCA(CreateView):
    template_name = 'trabajo/tabla-categoria/crear.html'
    model = tablaCategoria
    fields = ['categoria','hombre','mujer','total']
    success_url = reverse_lazy('trabajo')

class modificarTablaCA(UpdateView):
    template_name = 'trabajo/tabla-categoria/crear.html'
    model = tablaCategoria
    fields = ['categoria','hombre','mujer','total']
    success_url = reverse_lazy('trabajo')

class eliminarTablaCA(DeleteView):
    template_name = 'trabajo/tabla-categoria/crear.html'
    model = tablaCategoria
    fields = ['categoria','hombre','mujer','total']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('trabajo')


