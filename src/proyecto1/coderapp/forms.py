from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20, required=False)
    camada = forms.IntegerField()


class EstudianteBusqueda(forms.Form):
    email = forms.EmailField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
