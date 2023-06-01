from django.urls import path
from . import views

urlpatterns = [
    path('educacion/educacion', views.tablas, name = 'educacion'),
]