from django import forms
from .models import DatosCita

class SolicitarCitaForm(forms.ModelForm):
    fecha_cita = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'])

    class Meta:
        model = DatosCita
        fields = ('fecha_cita','talla','medio_comunicacion','descripcion_complementaria')
