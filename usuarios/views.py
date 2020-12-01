from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.conf import settings    
# our classes and function
from .forms import UsuarioRegisterForm, LoginForm, UpdatePasswordForm, VerificationForm
from .models import Usuarios
from .functions import code_generator

# Create your views here.

class UsuarioRegisterView(FormView):
    template_name = "usuarios/register.html"
    form_class = UsuarioRegisterForm
    success_url = '/'

    def form_valid(self, form):
        #generamos el codigo
        codigo = code_generator()

        usuario = Usuarios.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            codregistro=codigo
        )
        # enviar el codigo al email del user
        asunto = "Confirmacion de email"
        mensaje = "codigo de verificacion " + codigo
        email_remitente = settings.EMAIL_HOST_USER 
        # 
        to = form.cleaned_data['email']
        send_mail(asunto, mensaje, email_remitente, [to], fail_silently=False)
        # redirigir a pantalla de validacion
        return HttpResponseRedirect(
            reverse(
                'verification',
                kwargs={'pk': usuario.id}
            )
        )
        # return super(UsuarioRegisterView, self).form_valid(form)

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


class CodeVerificationView(FormView):
    template_name = "usuarios/verificacion.html"
    form_class = VerificationForm
    success_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk' : self.kwargs['pk']
        })
        return kwargs

    def form_valid(self, form):
        Usuarios.objects.filter(
            id=self.kwargs['pk']
        )
        return super(CodeVerificationView, self).form_valid(form)