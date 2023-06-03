from django.urls import path
from . import views

#app_name = 'trabajo_app'
urlpatterns = [
    path('trabajo/trabajo', views.tablas, name='trabajo'),
    
    #---------------- URLS DEL CRUD TABLA NIVEL -------------------------------------------------------
    path('trabajo/tabla-nivel/crear', views.crearTablaN.as_view(), name='Ncrear'),
    path('trabajo/tabla-nivel/modificar/<pk>/', views.modificarTablaN.as_view(), name='Nmodificar'),
    path('trabajo/tabla-nivel/eliminar/<pk>/', views.eliminarTablaN.as_view(), name='Neliminar'),

    #----------------- URLS DEL CRUD ENCUESTA UBBANA -------------------------------------------------
    path('trabajo/encuesta-urbana/crear', views.crearTablaUR.as_view(), name='URcrear'),
    path('trabajo/encuesta-urbana/modificar/<pk>/', views.modificarTablaUR.as_view(), name='URmodificar'),
    path('trabajo/encuesta-urbana/eliminar/<pk>/', views.eliminarTablaUR.as_view(), name='UReliminar'),

    #----------------- URLS DEL CRUD ENCUESTA RURAL -------------------------------------------------
    path('trabajo/encuesta-rural/crear', views.crearTablaRU.as_view(), name='RUcrear'),
    path('trabajo/encuesta-rural/modificar/<pk>/', views.modificarTablaRU.as_view(), name='RUmodificar'),
    path('trabajo/encuesta-rural/eliminar/<pk>/', views.eliminarTablaRU.as_view(), name='RUeliminar'),

     #----------------- URLS DEL CRUD TIPO DISCAPACIDAD -------------------------------------------------
    path('trabajo/tipo-disc/crear', views.crearTablaDI.as_view(), name='DIcrear'),
    path('trabajo/tipo-disc/modificar/<pk>/', views.modificarTablaDI.as_view(), name='DImodificar'),
    path('trabajo/tipo-disc/eliminar/<pk>/', views.eliminarTablaDI.as_view(), name='DIeliminar'),

     #----------------- URLS DEL CRUD CATEGORIA -------------------------------------------------
    path('trabajo/tabla-categoria/crear', views.crearTablaCA.as_view(), name='CAcrear'),
    path('trabajo/tabla-categoria/modificar/<pk>/', views.modificarTablaCA.as_view(), name='CAmodificar'),
    path('trabajo/tabla-categoria/eliminar/<pk>/', views.eliminarTablaCA.as_view(), name='CAeliminar'),

]