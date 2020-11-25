from django import forms
from .models import Usuarios

class UsuarioRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )

    class Meta:


        model = Usuarios
        fields = ('username', 'email', 'first_name','last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

         # TODO Validation

        if password1 != password2 :
            self.add_error('password2', 'Las contraseñas no son iguales' )
        else:
            if len(password2) < 9:
                self.add_error('password12', 'Las contraseñas deben tener como minimo 9 digito')


class LoginForm(forms.Form):
    """LoginForm definition."""

    # TODO: Define form fields here
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'style': '{ margin: 10px }',
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
