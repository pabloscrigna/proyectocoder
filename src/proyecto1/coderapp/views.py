from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Profesor, Curso
from coderapp.forms import CursoFormulario

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


def profesores(request):
    return render(request, 'profesores.html')


def estudiantes(request):
    return render(request, 'estudiantes.html')


def cursos(request):
    return render(request, 'cursos.html')


def entregables(request):
    return render(request, 'entregables.html')

"""
def curso_formulario(request):

    # path de la ruta
    print(f"path: {request.path}")
    print(f"full path: {request.get_full_path()}")
    print(f"host: {request.get_host()}")
    print(f"si es segura: {request.is_secure()}")
    print(f"metodo: {request.method}")
    ua = request.META.get("HTTP_USER_AGENT")
    print(f"ua: {ua}")

    if request.method == "POST":

        nombre = request.POST.get("curso")
        camada = request.POST.get("camada")

        print(f"El curso: {nombre} y la camada {camada}")

        curso = Curso(nombre=nombre, camada=camada)

        curso.save()

        return render(request, 'index.html')


    return render(request, 'curso_formulario.html')
"""


def curso_formulario(request):

    if request.method == "POST":

        formulario = CursoFormulario(request.POST) 

        # print("formulario")
        # print(formulario)


        print(f" is valid: {formulario.is_valid}")
        if formulario.is_valid():

            datos = formulario.cleaned_data

            nombre = datos.get("curso")
            camada = datos.get("camada")

            curso = Curso(nombre=nombre,camada=camada)

            curso.save()

            return render(request, 'index.html')

    else:
        formulario = CursoFormulario()

    return render(request, 'curso_formulario.html', {"formulario": formulario})

def busqueda_camada(request):

    if request.method == "GET":

        camada = request.GET.get("camada")
        print(f"Vamos a buscar la camada: {camada}")



    return render(request, 'busqueda_camada.html')


def buscar_camada(request):

    if request.method == "GET":

        camada = request.GET.get("camada")   ## ["camada"]

        if camada is None: 
            return HttpResponse("Enviar la camada a buscar")
        
        # Siguiente paso buscar los datos

        cursos = Curso.objects.filter(camada__icontains=camada)
        cursos = Curso.objects.filter(camada__lte=23)

        contexto = {
            "cursos": cursos,
            "camada": camada 
        }

        return render(request, "busqueda.html", contexto)