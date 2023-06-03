from django.shortcuts import render

# Create your views here.

def acerca_de(request):
    return render(request, 'acerca-de/acerca-de.html')
