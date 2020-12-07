from django.urls import path
from .views import PersonalizarProductoView, SolicitarCitaView, HistorialPagosVIew

urlpatterns = [
    path('personalizar-producto', PersonalizarProductoView.as_view(), name="personalizar_producto"),
    path('historial-pagos', HistorialPagosVIew.as_view(), name="historial_pagos"),
    path('solicitar-cita', SolicitarCitaView.as_view(), name="solicitar_cita"),
]