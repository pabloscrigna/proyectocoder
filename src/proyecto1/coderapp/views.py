from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Profesor

def leer_profesor(request):

    print("Vista profesor")
    profe = Profesor(nombre="John", apellido="Doe", email="doe@test.com")
    profe.save()    
    return HttpResponse("El profesor se creo exitosamente")


def leer_alumnos(request):

    contexto = {
        "nombre": "Juan",
        "apellido": "Hernandez",
        "edad": 6,
        "cursos": ["python", "C", "java"],
    }

    return render(request, 'plantilla.html', contexto)


def index(request):
    return render(request, 'index.html')
