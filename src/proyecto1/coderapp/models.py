from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Profesores"
        ordering=["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str_(self):
        return f"{self.nombre}, {self.apellido}"


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} --- {self.camada}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField(verbose_name="Fecha de Entrega")
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} --- {self.entregado}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"