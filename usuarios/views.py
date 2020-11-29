from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import UsuarioRegisterForm, LoginForm, UpdatePasswordForm
from .models import Usuarios
from django.http import HttpResponseRedirect

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

class LogoutVIew(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'usuarios/update.html'
    login_url = reverse_lazy('login')
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)