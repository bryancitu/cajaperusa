from django.urls import path
from .views import *

urlpatterns = [
    path('personalizar-producto', PersonalizarProductoView.as_view(), name="personalizar_producto"),
    path('historial-pagos', HistorialPagosVIew.as_view(), name="historial_pagos"),
    path('metodos-de-pago', PaymentPageVIew.as_view(), name="payment_page"),
    # paginas de los diferente tipos de productos
    path('cualquier-tipo-diseño', CualquierTipoDisenoView.as_view(), name="cualquier_tipo_diseno"),
    path('diseño-impresión-papel', DisenoImpresionPapelView.as_view(), name="diseno_impresion_papel"),
    path('diseño-impresión-objeto', DisenoImpresionObjetoView.as_view(), name="diseno_impresion_objeto"),
    path('impresion-objeto', ImpresionObjetoView.as_view(), name="impresion_objeto"),
    # paginas de solicitudes 
    path('solicitud-de-diseño-personalizado', SolicitudCualquierTipoDisenoView.as_view(), name="solicitud_cualquier_tipo_diseno"),
    path('solicitud-de-diseño-mas-impresión-papel', SolicitudDesignImpresionPapelView.as_view(), name="solicitud_de_diseño_mas_impresión_papel"),
    path('solicitud-de-diseño-mas-impresión-objeto', SolicitudDesignImpresionObjetoView.as_view(), name="solicitud_de_diseño_mas_impresión_objeto"),
    path('solicitud-de-impresión-objeto', SolicitudImpresionObjetoView.as_view(), name="solicitud_de_impresión_objeto"),
    # paginas de editar solicitudes
    path('editar-solicitud-de-diseño-personalizado/<pk>', EditarSolicitudCualquierTipoDisenoView.as_view(), name="editar_solicitud_cualquier_tipo_diseno"),
    path('editar-solicitud-de-diseño-mas-impresión-papel/<pk>', EditarSolicitudDesignImpresionPapelView.as_view(), name="editar_solicitud_de_diseño_mas_impresión_papel"),
    path('editar-solicitud-de-diseño-mas-impresión-objeto/<pk>', EditarSolicitudDesignImpresionObjetoView.as_view(), name="editar_solicitud_de_diseño_mas_impresión_objeto"),
    path('editar-solicitud-de-impresión-objeto/<pk>', EditarSolicitudImpresionObjetoView.as_view(), name="editar_solicitud_de_impresión_objeto"),
]