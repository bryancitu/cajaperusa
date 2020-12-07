from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
import datetime
import pytz

from .forms import *
from .models import DatosCita
from usuarios.models import Usuarios
# Create your views here.


class PersonalizarProductoView(TemplateView):
    template_name = "producto/personalizar_producto.html"
    pass


class SolicitarCitaView(TemplateView):
    template_name = "producto/solicitar_cita.html"
    
    def get_context_data(self, **kwargs):
        form = SolicitarCitaForm
        kwargs['form'] = form
        return kwargs
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = Usuarios.objects.filter(id=self.request.user.id).first()
        form = SolicitarCitaForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            solicitud.usuario = user
            solicitud.save()
            user.monto_pagar += 85
            user.save()
            messages.success(request, 'Envio de Solicitud de cita correctamente!')
            return redirect('home')
        context['form'] = form
        messages.error(request, 'Completar el formulario correctamente!')
        return self.render_to_response(context)


class HistorialPagosVIew(TemplateView):
    template_name = "producto/historial_pagos.html"
    pass
