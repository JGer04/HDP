from django.urls import path
from . import views

urlpatterns = [
    path('referencia/referencia', views.referencia, name = 'referencia')
]
