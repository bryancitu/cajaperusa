from django.urls import path
from .views import PersonalizarProductoView, SolicitarCitaView

urlpatterns = [
    path('personalizar-producto', PersonalizarProductoView.as_view(), name="personalizar_producto"),
    path('solicitar-cita', SolicitarCitaView.as_view(), name="solicitar_cita"),
]