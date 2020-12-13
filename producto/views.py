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


# Paginas de los 4 diferentes productos que tenemos
class CualquierTipoDisenoView(TemplateView):
    template_name = "producto/cualquier_tipo_diseno.html"
    pass

class DisenoImpresionPapelView(TemplateView):
    template_name = "producto/diseno_impresion_papel.html"
    pass

class DisenoImpresionObjetoView(TemplateView):
    template_name = "producto/diseno_impresion_objeto.html"
    pass

class ImpresionObjetoView(TemplateView):
    template_name = "producto/impresion_objeto.html"
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
            messages.success(request, 'Envio de Solicitud de cita correctamente!')
            return redirect('home')
        context['form'] = form
        messages.error(request, 'Completar el formulario correctamente!')
        return self.render_to_response(context)

class HistorialPagosVIew(TemplateView):
    template_name = "producto/historial_pagos.html"
    
    def get_context_data(self, **kwargs):
        user = Usuarios.objects.filter(id=self.request.user.id).first()
        solicitudes = DatosCita.objects.filter(usuario = user)
        cantidad_solicitud = DatosCita.objects.filter(usuario = user).count()
        kwargs['solicitudes'] = solicitudes
        kwargs['cantidad_solicitud'] = cantidad_solicitud
        return kwargs


# Solicitudes de los 4
class SolicitudCualquierTipoDisenoView(TemplateView):
    template_name = "producto/solicitud_cualquier_tipo_diseno.html"
    
    def get_context_data(self, **kwargs):
        form = SolicitudDisenoForm
        kwargs['form'] = form
        return kwargs
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = Usuarios.objects.filter(id=self.request.user.id).first()
        form = SolicitudDisenoForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            solicitud.usuario = user
            solicitud.save()
            messages.success(request, 'Envio de Solicitud de cita correctamente!')
            return redirect('home')
        context['form'] = form
        messages.error(request, 'Completar el formulario correctamente!')
        return self.render_to_response(context)

class SolicitudDisenoImpresionPapelView(TemplateView):
    template_name = "producto/solicitud_diseno_impresion_papel.html"
    pass

class SolicitudDisenoImpresionObjetoView(TemplateView):
    template_name = "producto/solicitud_diseno_impresion_objeto.html"
    pass

class SolicitudImpresionObjetoView(TemplateView):
    template_name = "producto/solicitud_impresion_objeto.html"
    pass

    
