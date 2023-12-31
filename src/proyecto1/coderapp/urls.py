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
)

urlpatterns = [
    path("profesores/", profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path("cursos/", cursos, name='cursos'),
    path('entregables/', entregables, name='entregables'),
    path('cursoFormulario', curso_formulario, name='curso_formulario' ),
    path('busquedaCamada', busqueda_camada, name="busqueda_camada"),
    path("buscar", buscar_camada, name='buscar_camada'),
    path("", index, name='index' ),
]