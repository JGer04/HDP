from django.urls import path
from . import views

urlpatterns = [
    path('trabajo/trabajo', views.tablas, name='trabajo'),
    path('trabajo/modificar', views.crearTabla.as_view(), name='modificar'),
]