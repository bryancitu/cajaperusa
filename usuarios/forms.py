from django import forms
from .models import Usuarios

class UsuarioRegisterForm(forms.ModelForm):

    class Meta:

        model = Usuarios
        fields = ("__all__")