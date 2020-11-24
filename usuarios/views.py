from django.shortcuts import render

from django.views.generic.edit import FormView
from .forms import UsuarioRegisterForm
from .models import Usuarios

# Create your views here.


class UsuarioRegisterView(FormView):
    template_name = "usuarios/register.html"
    form_class = UsuarioRegisterForm
    success_url = '/'

    def form_valid(self, form):

        Usuarios.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )

        return super(UsuarioRegisterView, self).form_valid(form)