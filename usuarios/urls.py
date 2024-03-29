from django.urls import path
from .views import UsuarioRegisterView, LoginUsuario, LogoutVIew, UpdatePasswordView, CodeVerificationView


urlpatterns = [
    path('registrarse/', UsuarioRegisterView.as_view(),name='registrarse'),
    path('login/', LoginUsuario.as_view(),name='login'),
    path('logout/', LogoutVIew.as_view(),name='logout'),
    path('update/', UpdatePasswordView.as_view(),name='update'),
    path('verification/<pk>/', CodeVerificationView.as_view(),name='verification'),
]
