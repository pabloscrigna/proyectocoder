from django.urls import path

from coderapp.views import profesores, estudiantes, cursos, entregables, index

urlpatterns = [
    path("profesores/", profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path("cursos/", cursos, name='cursos'),
    path('entregables/', entregables, name='entregables'),
    path("", index, name='index' )
]