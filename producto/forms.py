from django import forms
from .models import *
from design.models import Design

class SolicitudDisenoForm(forms.ModelForm):
    fecha_cita                 = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.TextInput(attrs={'autocomplete': 'off',}))
    descripcion_complementaria = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: vertical; height: 15rem;width: calc(100% - 3rem)',}))
    design                     = forms.ModelChoiceField(label='Elege tu Diseñador',queryset=Design.objects.all(),widget=forms.RadioSelect() )

    class Meta:
        model = SolicitudDiseno
        fields = ('fecha_cita','formato_img','medio_comunicacion','design','descripcion_complementaria')


class SolicitudDesignImpresionPapelForm(forms.ModelForm):
    fecha_cita                 = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.TextInput(attrs={'autocomplete': 'off',}))
    descripcion_complementaria = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: vertical; height: 15rem;width: calc(100% - 3rem)',}))
    design                     = forms.ModelChoiceField(label='Elege tu Diseñador',queryset=Design.objects.all(),widget=forms.RadioSelect() )

    class Meta:
        model = SolicitudDesignImpresionPapel
        fields = ('fecha_cita','size','type_print','type_paper','medio_comunicacion','design','descripcion_complementaria')


class SolicitudDesignImpresionObjetoForm(forms.ModelForm):
    fecha_cita                 = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.TextInput(attrs={'autocomplete': 'off',}))
    descripcion_complementaria = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: vertical; height: 15rem;width: calc(100% - 3rem)',}))
    design                     = forms.ModelChoiceField(label='Elege tu Diseñador',queryset=Design.objects.all(),widget=forms.RadioSelect() )

    class Meta:
        model = SolicitudDesignImpresionObjeto
        fields = ('fecha_cita','object_print','medio_comunicacion','design','descripcion_complementaria')


class SolicitudImpresionObjetoForm(forms.ModelForm):
    fecha_cita                 = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],widget=forms.TextInput(attrs={'autocomplete': 'off',}))
    descripcion_complementaria = forms.CharField(widget=forms.Textarea(attrs={'style': 'resize: vertical; height: 15rem;width: calc(100% - 3rem)',}))
    design                     = forms.ModelChoiceField(label='Elege tu Diseñador',queryset=Design.objects.all(),widget=forms.RadioSelect() )

    class Meta:
        model = SolicitudImpresionObjeto
        fields = ('fecha_cita','object_print','medio_comunicacion','design','descripcion_complementaria')

