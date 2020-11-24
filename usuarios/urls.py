from django.urls import path
from .views import UsuarioRegisterView


urlpatterns = [
    path('registrarse/', UsuarioRegisterView.as_view(),name='registrarse'),
]
