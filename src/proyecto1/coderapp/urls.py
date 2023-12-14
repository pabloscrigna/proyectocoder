from django.urls import path

from coderapp.views import leer_profesor, leer_alumnos

urlpatterns = [
    path("profesores/", leer_profesor ),
    path('alumnos/', leer_alumnos),
]