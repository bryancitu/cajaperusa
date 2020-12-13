from django.urls import path
from .views import *

urlpatterns = [
    path('personalizar-producto', PersonalizarProductoView.as_view(), name="personalizar_producto"),
    path('historial-pagos', HistorialPagosVIew.as_view(), name="historial_pagos"),
    path('solicitar-cita', SolicitarCitaView.as_view(), name="solicitar_cita"),
    path('cualquier-tipo-diseño', CualquierTipoDisenoView.as_view(), name="cualquier_tipo_diseno"),
    path('diseño-impresión-papel', DisenoImpresionPapelView.as_view(), name="diseno_impresion_papel"),
    path('diseño-impresión-objeto', DisenoImpresionObjetoView.as_view(), name="diseno_impresion_objeto"),
    path('impresion-objeto', ImpresionObjetoView.as_view(), name="impresion_objeto"),
]