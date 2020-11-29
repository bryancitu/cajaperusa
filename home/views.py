import datetime
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context


class HomePage(TemplateView):
    template_name = "home/index.html"


class TemplatePruebaMixin(LoginRequiredMixin,TemplateView):
    template_name = "home/mixin.html"
    login_url = reverse_lazy('login')
