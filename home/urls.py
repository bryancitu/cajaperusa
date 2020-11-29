from django.urls import path
from .views import HomePage, TemplatePruebaMixin


urlpatterns = [
    path('', HomePage.as_view(),name='home'),
    path('mixin/', TemplatePruebaMixin.as_view(),name='mixin'),
]
