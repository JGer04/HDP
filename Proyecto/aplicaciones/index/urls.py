from django.urls import path
from . import views

urlpatterns = [
    path('index/inicio', views.index, name='inicio'),
]