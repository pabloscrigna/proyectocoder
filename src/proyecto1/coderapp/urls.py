from django.urls import path
from django.contrib.auth.views import LogoutView

from coderapp.views import (
    profesores,
    estudiantes,
    cursos,
    entregables,
    index,
    curso_formulario,
    busqueda_camada,
    buscar_camada,
    leer_profesores,
    eliminar_profesor,
    editar_profesor,
    login_request,
    registrar,
    editar_perfil,
    CursoList,
    CursoDetalle,
    CursoCreacion,
    CursoUpdate,
    CursoDelete
)

urlpatterns = [
    path("profesores/", profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path("cursos/", cursos, name='cursos'),
    path('entregables/', entregables, name='entregables'),
    path('cursoFormulario', curso_formulario, name='curso_formulario'),
    path('busquedaCamada', busqueda_camada, name="busqueda_camada"),
    path("buscar", buscar_camada, name='buscar_camada'),
    path("leerProfesores", leer_profesores, name='leer_profesores'),
    path('eliminarProfesor/<nombre_profesor>', eliminar_profesor, name="eliminar_profesor"),
    path('editar_profesor/<nombre_profesor>', editar_profesor, name='editar_profesor'),
    path('curso/list', CursoList.as_view(), name='List'),
    path('detalle-curso/<pk>', CursoDetalle.as_view(), name='Detail'),
    path("editar-curso/<pk>", CursoUpdate.as_view(), name='Edit'),
    path("crear-curso", CursoCreacion.as_view(), name='New'),
    path("borrar-cursos/<pk>", CursoDelete.as_view(), name='Delete'),
    path("login", login_request, name='Login'),
    path("registrar", registrar, name='Registrar'),
    path("logout", LogoutView.as_view(template_name="logout.html"), name='Logout'),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
    path("", index, name='index'),
]