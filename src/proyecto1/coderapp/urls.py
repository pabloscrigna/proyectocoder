from django.urls import path

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
    path('curso/list', CursoList.as_view(), name='List'),
    path('detalle-curso/<pk>', CursoDetalle.as_view(), name='Detail'),
    path("editar-curso/<pk>", CursoUpdate.as_view(), name='Edit'),
    path("borrar-cursos/<pk>", CursoDelete.as_view(), name='Delete'),
    path("", index, name='index'),
]