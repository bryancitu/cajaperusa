from django.shortcuts import render

from django.views.generic import CreateView
from .forms import UsuarioRegisterForm

# Create your views here.


class UsuarioRegisterView(CreateView):
    template_name = "usuarios/register.html"
    form_class = UsuarioRegisterForm
    success_url = '/'