from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Profesor, Curso, Avatar
from coderapp.forms import (
    CursoFormulario, 
    ProfesorFormulario, 
    UserRegistrationForm,
    UserEditForm,
    AvatarFormulario,
)

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        return render(request, 'index.html', {"url": avatar[0].image.url})

    return render(request, 'index.html')

@login_required
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

def editar_profesor(request, nombre_profesor):

    profesor = Profesor.objects.get(nombre=nombre_profesor)


    if request.method == "POST":
        
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            datos_profesor = formulario.cleaned_data

            profesor.nombre = datos_profesor.get("nombre")
            profesor.apellido = datos_profesor.get("apellido")
            profesor.email = datos_profesor.get("email")

            profesor.save()

            return render(request, 'index.html')

    formulario = ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email})

    return render(request, "editar_profesor.html", {"formulario": formulario, "profesor_nombre": nombre_profesor})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})                
            else:
                return render(request, 'index.html', {"mensaje": f"Usuario o contraseña invalidos"})

        else:
            return render(request, "index.html", {"mensaje": "Datos form incorrectos"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def registrar(request):

    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")
            
            form.save()

            return render(request, "index.html", {"mensaje": f"Se dio de alta el usuario {username}"} )

    # form = UserCreationForm()
    form = UserRegistrationForm()    

    return render(request, "registro.html", {"form": form})


@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion.get("email")
            usuario.password1 = informacion.get("password1")
            usuario.password2 = informacion.get("password2")
            usuario.last_name = informacion.get("last_name")
            usuario.first_name = informacion.get("first_name")

            usuario.save()

            return render(request, "index.html")

    formulario = UserEditForm(initial={"email": usuario.email })

    return render(request, "editar_usuario.html", {"formulario": formulario}) 

@login_required
def avatar(request):

    if request.method == "POST":
        print("Post")
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            user = User.objects.get(username=request.user)   
            avatar = Avatar(user=user, image=formulario.cleaned_data.get("image"))
            avatar.save()

            return render(request, 'index.html')

    formulario = AvatarFormulario()

    return render(request, 'avatar.html', {"formulario": formulario})


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


