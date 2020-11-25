from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import UsuarioRegisterForm, LoginForm
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


class LoginUsuario(FormView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUsuario, self).form_valid(form)