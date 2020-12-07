from django.db import models
from ckeditor.fields import RichTextField
from usuarios.models import Usuarios

# Create your models here.

class BaseModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DatosCita(BaseModel):

    TALLAS = (
        ('S' , 'Small'),
        ('M' , 'Medium'),
        ('L' , 'Large'),
        ('XL', 'XL-Large'),
    )

    MEDIOS_COMUNICACION = (
        ('Zoom', 'Zoom'),
        ('WhatsApp', 'WhatsApp'),
        ('FB-messenger', 'FB-messenger'),
    )

    usuario                     = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True) 
    fecha_cita                  = models.DateTimeField('Fecha de la Cita',auto_now=False, auto_now_add=False)
    talla                       = models.CharField('Talla',max_length=50, choices=TALLAS)
    medio_comunicacion          = models.CharField('Medio de Comunicación',max_length=50, choices=MEDIOS_COMUNICACION)
    descripcion_complementaria  = RichTextField(blank=True,)


    class Meta:
        verbose_name = 'DatosCita'
        verbose_name_plural = 'DatosCitas'

    def __str__(self):
        return str(self.usuario)
