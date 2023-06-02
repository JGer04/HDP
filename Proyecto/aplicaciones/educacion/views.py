from django.shortcuts import render
from.models import *
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
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

# -------------------- CRUD DE TABLA ESTUDIANTS ACTIVOS IES ------------------------------
class crearTablaAC(CreateView):
    template_name = 'educacion/tabla-activos/crear.html'
    model = Estudiantes_Activos_IES
    fields = ['año','fisica','intelectual','sensorial','mental','total']
    success_url = reverse_lazy('educacion')

class modificarTablaAC(UpdateView):
    template_name = 'educacion/tabla-activos/modificar.html'
    model = Estudiantes_Activos_IES
    fields = ['año','fisica','intelectual','sensorial','mental','total']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('educacion')

class eliminarTablaAC(DeleteView):
    template_name = 'educacion/tabla-activos/eliminar.html'
    model = Estudiantes_Activos_IES
    fields = ['año','fisica','intelectual','sensorial','mental','total']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('educacion')

# -------------------- CRUD DE TABLA ESTUDIANTES POR GENERO Y DISPACIDAD (2018) ------------------------------
class crearTabla18(CreateView):
    template_name = 'educacion/tabla-2018/crear.html'
    model = Estudiantes_Genero_Tipo_2018
    fields = ['discapacidad','masculino','femenino']
    success_url = reverse_lazy('educacion')

class modificarTabla18(UpdateView):
    template_name = 'educacion/tabla-2018/modificar.html'
    model = Estudiantes_Genero_Tipo_2018
    fields = ['discapacidad','masculino','femenino']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('educacion')

class eliminarTabla18(DeleteView):
    template_name = 'educacion/tabla-2018/eliminar.html'
    model = Estudiantes_Genero_Tipo_2018
    fields = ['discapacidad','masculino','femenino']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('educacion')

# -------------------- CRUD DE TABLA ESTUDIANTES POR GENERO Y DISPACIDAD (2019) ------------------------------
class crearTabla19(CreateView):
    template_name = 'educacion/tabla-2019/crear.html'
    model = Estudiantes_Genero_Tipo_2019
    fields = ['discapacidad','masculino','femenino']
    success_url = reverse_lazy('educacion')

class modificarTabla19(UpdateView):
    template_name = 'educacion/tabla-2019/modificar.html'
    model = Estudiantes_Genero_Tipo_2019
    fields = ['discapacidad','masculino','femenino']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('educacion')

class eliminarTabla19(DeleteView):
    template_name = 'educacion/tabla-2019/eliminar.html'
    model = Estudiantes_Genero_Tipo_2019
    fields = ['discapacidad','masculino','femenino']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('educacion')

# -------------------- CRUD DE TABLA ESTUDIANTES POR GENERO Y DISPACIDAD (2020) ------------------------------
class crearTabla20(CreateView):
    template_name = 'educacion/tabla-2020/crear.html'
    model = Estudiantes_Genero_Tipo_2020
    fields = ['discapacidad','masculino','femenino']
    success_url = reverse_lazy('educacion')

class modificarTabla20(UpdateView):
    template_name = 'educacion/tabla-2020/modificar.html'
    model = Estudiantes_Genero_Tipo_2020
    fields = ['discapacidad','masculino','femenino']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('educacion')

class eliminarTabla20(DeleteView):
    template_name = 'educacion/tabla-2020/eliminar.html'
    model = Estudiantes_Genero_Tipo_2020
    fields = ['discapacidad','masculino','femenino']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('educacion')

# -------------------- CRUD DE TABLA DE PREVALENCIA DE DISCAPACIDAD ------------------------------
class crearTablaPR(CreateView):
    template_name = 'educacion/tabla-preva/crear.html'
    model = Prevalencia_Estudiantes_Activos_IES
    fields = ['discapacidad','año_2018','año_2019','año_2020','total','porcentaje']
    success_url = reverse_lazy('educacion')

class modificarTablaPR(UpdateView):
    template_name = 'educacion/tabla-preva/modificar.html'
    model = Prevalencia_Estudiantes_Activos_IES
    fields = ['discapacidad','año_2018','año_2019','año_2020','total','porcentaje']
    success_message = "El registro %(nombre)s fue mofificado exitosamente"
    success_url = reverse_lazy('educacion')

class eliminarTablaPR(DeleteView):
    template_name = 'educacion/tabla-preva/eliminar.html'
    model = Prevalencia_Estudiantes_Activos_IES
    fields = ['discapacidad','año_2018','año_2019','año_2020','total','porcentaje']
    success_message = "El registro %(nombre)s fue eliminado exitosamente"
    success_url = reverse_lazy('educacion')

