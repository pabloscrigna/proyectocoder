from django.contrib import admin

from coderapp.models import (
    Profesor,
    Curso,
    Estudiante,
    Entregable,
)

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Entregable)
