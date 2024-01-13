from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=20, required=False)
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2", "last_name", "first_name"]


class UserEditForm(forms.Form):
    email = forms.EmailField(label="Ingesar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User 
        fields = [ "email", "password1", "password2", "last_name", "first_name"]

class AvatarFormulario(forms.Form):
    image = forms.ImageField()

    