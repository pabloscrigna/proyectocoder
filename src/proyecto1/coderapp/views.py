from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Profesor, Curso
from coderapp.forms import CursoFormulario, ProfesorFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    
    if request.method == "POST":
        
        # leer los datos que vienen en el post
        datos_profesor = ProfesorFormulario(request.POST)

        print(datos_profesor)

        if datos_profesor.is_valid():

            datos = datos_profesor.cleaned_data

            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")

            profesor = Profesor(nombre=nombre, apellido=apellido, email=email)
            profesor.save()

            return render(request, 'index.html')

    else:
        profesorFormulario = ProfesorFormulario()

    return render(request, 'crear_profesor.html', {"profesorFormulario": profesorFormulario})


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

            curso = Curso(nombre=nombre, camada=camada)

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
    

def leer_profesores(request):

    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}


    return render(request, 'leer_profesores.html', contexto)


def eliminar_profesor(request, nombre_profesor):

    profesor = Profesor.objects.get(nombre=nombre_profesor)

    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}

    return render(request, 'leer_profesores.html', contexto)


# Vistas basadas en clases para el modelo Curso

class CursoList(ListView):

    model = Curso
    template_name = 'cursos_list.html'


class CursoDetalle(DetailView):

    model = Curso
    template_name = 'curso_detalle.html'


class CursoCreacion(CreateView):

    model = Curso
    fields = ['nombre', 'camada']
    template_name = 'curso_form.html'
    success_url = "/coder-app/curso/list"


class CursoUpdate(UpdateView):
    
    model = Curso
    fields = ['nombre', 'camada']
    template_name = 'curso_form.html'
    success_url ="/coder-app/curso/list"

class CursoDelete(DeleteView):
    
    model = Curso
    template_name = "curso_confirm_delete.html"
    success_url = "/coder-app/curso/list"


