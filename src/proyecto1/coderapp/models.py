from django.db import models


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
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} --- {self.entregado}"
