from django.urls import path
from . import views

urlpatterns = [
    path('educacion/educacion', views.tablas, name = 'educacion'),

    #---------------- URLS DEL CRUD TABLA ESTUDIANTES ACTIVOS IES -------------------------------------------------------
    path('educacion/tabla-activos/crear', views.crearTablaAC.as_view(), name='ACcrear'),
    path('educacion/tabla-activos/modificar/<pk>/', views.modificarTablaAC.as_view(), name='ACmodificar'),
    path('educacion/tabla-activos/eliminar/<pk>/', views.eliminarTablaAC.as_view(), name='ACeliminar'),

    #---------------- URLS DEL CRUD DE TABLA ESTUDIANTES POR GENERO Y DISPACIDAD (2018) -------------------------------------------------------
    path('educacion/tabla-2018/crear', views.crearTabla18.as_view(), name='18crear'),
    path('educacion/tabla-2018/modificar/<pk>/', views.modificarTabla18.as_view(), name='18modificar'),
    path('educacion/tabla-2018/eliminar/<pk>/', views.eliminarTabla18.as_view(), name='18eliminar'),

    #---------------- URLS DEL CRUD DE TABLA ESTUDIANTES POR GENERO Y DISPACIDAD (2019) -------------------------------------------------------
    path('educacion/tabla-2019/crear', views.crearTabla19.as_view(), name='19crear'),
    path('educacion/tabla-2019/modificar/<pk>/', views.modificarTabla19.as_view(), name='19modificar'),
    path('educacion/tabla-2019/eliminar/<pk>/', views.eliminarTabla19.as_view(), name='19eliminar'),

    #---------------- URLS DEL CRUD DE TABLA ESTUDIANTES POR GENERO Y DISPACIDAD (2020) -------------------------------------------------------
    path('educacion/tabla-2020/crear', views.crearTabla20.as_view(), name='20crear'),
    path('educacion/tabla-2020/modificar/<pk>/', views.modificarTabla20.as_view(), name='20modificar'),
    path('educacion/tabla-2020/eliminar/<pk>/', views.eliminarTabla20.as_view(), name='20eliminar'),

    #---------------- URLS DEL CRUD DE TABLA DE PREVALENCIA DE DISCAPACIDAD -------------------------------------------------------
    path('educacion/tabla-preva/crear', views.crearTablaPR.as_view(), name='PRcrear'),
    path('educacion/tabla-preva/modificar/<pk>/', views.modificarTablaPR.as_view(), name='PRmodificar'),
    path('educacion/tabla-preva/eliminar/<pk>/', views.eliminarTablaPR.as_view(), name='PReliminar'),
    
]