from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
import datetime
import pytz

from .forms import *
from .models import *
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


class HistorialPagosVIew(LoginRequiredMixin,TemplateView):
    template_name = "producto/historial_pagos.html"

    def get_context_data(self, **kwargs):
        user = Usuarios.objects.filter(id=self.request.user.id).first()

        sld_cualquier_design    = SolicitudDiseno.objects.filter(usuario = user)
        sld_design_papel        = SolicitudDesignImpresionPapel.objects.filter(usuario = user)
        sld_design_objeto       = SolicitudDesignImpresionObjeto.objects.filter(usuario = user)
        sld_print_objeto        = SolicitudImpresionObjeto.objects.filter(usuario = user)

        ctd_cualquier_design    = SolicitudDiseno.objects.filter(usuario = user).count()
        ctd_design_papel        = SolicitudDesignImpresionPapel.objects.filter(usuario = user).count()
        ctd_design_objeto       = SolicitudDesignImpresionObjeto.objects.filter(usuario = user).count()
        ctd_print_objeto        = SolicitudImpresionObjeto.objects.filter(usuario = user).count()

        monto_cd = 0
        monto_dp = 0
        monto_do = 0
        monto_po = 0

        for solicitud in SolicitudDiseno.objects.filter(usuario = user):
            if solicitud.precio and not solicitud.pagado:
                monto_cd += solicitud.precio

        for solicitud in SolicitudDesignImpresionPapel.objects.filter(usuario = user):
            if solicitud.precio and not solicitud.pagado:
                monto_dp += solicitud.precio

        for solicitud in SolicitudDesignImpresionObjeto.objects.filter(usuario = user):
            if solicitud.precio and not solicitud.pagado:
                monto_do += solicitud.precio

        for solicitud in SolicitudImpresionObjeto.objects.filter(usuario = user):
            if solicitud.precio and not solicitud.pagado:
                monto_po += solicitud.precio
                

        print(monto_cd)

        kwargs['sld_cualquier_design']  = sld_cualquier_design
        kwargs['sld_design_papel']      = sld_design_papel
        kwargs['sld_design_objeto']     = sld_design_objeto
        kwargs['sld_print_objeto']      = sld_print_objeto

        kwargs['ctd_cualquier_design']  = ctd_cualquier_design
        kwargs['ctd_design_papel']      = ctd_design_papel
        kwargs['ctd_design_objeto']     = ctd_design_objeto
        kwargs['ctd_print_objeto']      = ctd_print_objeto

        kwargs['monto_cd'] = monto_cd
        kwargs['monto_dp'] = monto_dp
        kwargs['monto_do'] = monto_do
        kwargs['monto_po'] = monto_po

        kwargs['ctd_total']   = ctd_cualquier_design + ctd_design_papel + ctd_design_objeto + ctd_print_objeto
        kwargs['monto_total'] = monto_cd + monto_dp + monto_do + monto_po
        return kwargs


class PaymentPageVIew(LoginRequiredMixin,TemplateView):
    template_name = "producto/payment_page.html"

    # def get_context_data(self, **kwargs):
    #     form = SolicitudDisenoForm
    #     kwargs['form'] = form
    #     return kwargs



# Solicitudes de los 4
class SolicitudCualquierTipoDisenoView(LoginRequiredMixin,TemplateView):
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

class SolicitudDesignImpresionPapelView(LoginRequiredMixin,TemplateView):
    template_name = "producto/solicitud_diseno_impresion_papel.html"
    
    def get_context_data(self, **kwargs):
        form = SolicitudDesignImpresionPapelForm
        kwargs['form'] = form
        return kwargs
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = Usuarios.objects.filter(id=self.request.user.id).first()
        form = SolicitudDesignImpresionPapelForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            solicitud.usuario = user
            solicitud.save()
            messages.success(request, 'Envio de Solicitud de cita correctamente!')
            return redirect('home')
        context['form'] = form
        messages.error(request, 'Completar el formulario correctamente!')
        return self.render_to_response(context)

class SolicitudDesignImpresionObjetoView(LoginRequiredMixin,TemplateView):
    template_name = "producto/solicitud_diseno_impresion_objeto.html"
    
    def get_context_data(self, **kwargs):
        form = SolicitudDesignImpresionObjetoForm
        kwargs['form'] = form
        return kwargs
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = Usuarios.objects.filter(id=self.request.user.id).first()
        form = SolicitudDesignImpresionObjetoForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            solicitud.usuario = user
            solicitud.save()
            messages.success(request, 'Envio de Solicitud de cita correctamente!')
            return redirect('home')
        context['form'] = form
        messages.error(request, 'Completar el formulario correctamente!')
        return self.render_to_response(context)

class SolicitudImpresionObjetoView(TemplateView):
    template_name = "producto/solicitud_impresion_objeto.html"
    
    def get_context_data(self, **kwargs):
        form = SolicitudImpresionObjetoForm
        kwargs['form'] = form
        return kwargs
        
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = Usuarios.objects.filter(id=self.request.user.id).first()
        form = SolicitudImpresionObjetoForm(request.POST)
        if form.is_valid():
            solicitud = form.save()
            solicitud.usuario = user
            solicitud.save()
            messages.success(request, 'Envio de Solicitud de cita correctamente!')
            return redirect('home')
        context['form'] = form
        messages.error(request, 'Completar el formulario correctamente!')
        return self.render_to_response(context)

# Editar las 4 tipos de solicitudes
class EditarSolicitudCualquierTipoDisenoView(LoginRequiredMixin,UpdateView):
    template_name = "producto/editar_solicitud_cualquier_tipo_diseno.html"
    model = SolicitudDiseno
    fields = ('fecha_cita','formato_img','medio_comunicacion','design','descripcion_complementaria')
    success_url = reverse_lazy('historial_pagos')
    
class EditarSolicitudDesignImpresionPapelView(LoginRequiredMixin,UpdateView):
    template_name = "producto/editar_solicitud_cualquier_tipo_diseno.html"
    model = SolicitudDesignImpresionPapel
    fields = ('fecha_cita','size','type_print','type_paper','medio_comunicacion','design','descripcion_complementaria')
    success_url = reverse_lazy('historial_pagos')

class EditarSolicitudDesignImpresionObjetoView(LoginRequiredMixin,UpdateView):
    template_name = "producto/editar_solicitud_cualquier_tipo_diseno.html"
    model = SolicitudDesignImpresionObjeto
    fields = ('fecha_cita','object_print','medio_comunicacion','design','descripcion_complementaria')
    success_url = reverse_lazy('historial_pagos')

class EditarSolicitudImpresionObjetoView(LoginRequiredMixin,UpdateView):
    template_name = "producto/editar_solicitud_cualquier_tipo_diseno.html"
    model = SolicitudImpresionObjeto
    fields = ('fecha_cita','object_print','medio_comunicacion','design','descripcion_complementaria')
    success_url = reverse_lazy('historial_pagos')
