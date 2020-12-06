from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class PersonalizarProducto(TemplateView):
    template_name = "producto/personalizar_producto.html"
    pass