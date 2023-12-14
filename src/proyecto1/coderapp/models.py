from django.db import models


class Profesor(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
