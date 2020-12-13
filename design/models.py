from django.db import models
from usuarios.models import Usuarios
# Create your models here.

class Design(models.Model):

    usuario             = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True) 
    url_wsp             = models.URLField('Link de WhatsApp', max_length=500)
    url_zoom            = models.URLField('Link de Zoom', max_length=500)
    url_fb_messenger    = models.URLField('Link de Messenger de Facebook', max_length=500)


    class Meta:
        verbose_name = 'Diseñador'
        verbose_name_plural = 'Diseñadores'

    def __str__(self):
        return str(self.usuario)