from django.urls import path
from . import views

urlpatterns = [
    path('acerca-de/acerca-de', views.acerca_de, name = 'acerca_de')
]
