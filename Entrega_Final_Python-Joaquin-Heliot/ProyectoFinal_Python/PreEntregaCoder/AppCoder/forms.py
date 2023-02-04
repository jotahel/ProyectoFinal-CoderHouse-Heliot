from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ConsultasFormulario(forms.Form):

    consulta = forms.CharField(max_length=150)
    nombre = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    email = forms.EmailField()


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    #imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar e-mail")
    password1 = forms.CharField(label="Contraseña")
    password2 = forms.CharField(label="Modificar contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Modificar apellido")
    first_name = forms.CharField(label="Modificar nombre")

    class Meta:

        model = User
        fields = ['email', 'password1', 'password2']

