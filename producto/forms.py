from django import forms
from .models import *
from design.models import Design

class SolicitarCitaForm(forms.ModelForm):
    fecha_cita = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.TextInput(attrs={'autocomplete': 'off',}))

    class Meta:
        model = DatosCita
        fields = ('fecha_cita','talla','medio_comunicacion','descripcion_complementaria')


class SolicitudDisenoForm(forms.ModelForm):
    fecha_cita                 = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.TextInput(attrs={'autocomplete': 'off',}))
    descripcion_complementaria = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: vertical; height: 15rem;width: calc(100% - 3rem)',}))
    design                     = forms.ModelChoiceField(label='Elege tu Diseñador',queryset=Design.objects.all(),widget=forms.RadioSelect() )

    class Meta:
        model = SolicitudDiseno
        fields = ('fecha_cita','formato_img','medio_comunicacion','design','descripcion_complementaria')

