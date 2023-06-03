from django.shortcuts import render

# Create your views here.

def referencia(request):
    return render(request, 'referencia/referencia.html')
