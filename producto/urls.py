from django.urls import path
from .views import PersonalizarProducto

urlpatterns = [
    path('personalizar-producto', PersonalizarProducto.as_view(), name="personalizar_producto")
]