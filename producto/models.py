from django.db import models
from ckeditor.fields import RichTextField
from usuarios.models import Usuarios
from design.models import Design

# Create your models here.

class BaseModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        abstract = True

class SolicitudDiseno(BaseModel):

    FORMATO = (
        ('png' , 'png'),
        ('jpg' , 'jpg'),
        ('pdf' , 'pdf'),
        ('jpeg', 'jpeg'),
        ('svg' , 'svg'),
        ('illustrator (ai)', 'illustrator (ai)'),
        ('photoshop (psd)' , 'photoshop (psd)'),
    )

    MEDIOS_COMUNICACION = (
        ('Zoom', 'Zoom'),
        ('WhatsApp', 'WhatsApp'),
        ('FB-messenger', 'FB-messenger'),
    )

    usuario                     = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True) 
    fecha_cita                  = models.DateTimeField('Fecha de la Cita:',auto_now=False, auto_now_add=False)
    formato_img                 = models.CharField('Formato de la Imagen:',max_length=50, choices=FORMATO)
    medio_comunicacion          = models.CharField('Medio de Comunicación:',max_length=50, choices=MEDIOS_COMUNICACION)
    descripcion_complementaria  = RichTextField('Descripción Complementaria:',blank=True,)
    design                      = models.ForeignKey(Design, on_delete=models.CASCADE, blank=True, null=True)
    precio                      = models.DecimalField('Precio', max_digits=5, decimal_places=2,blank=True, null=True)
    pagado                      = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Solicitud Diseño'
        verbose_name_plural = 'Solicitudes Diseños'

    def __str__(self):
        return str(self.usuario)

class SolicitudDesignImpresionPapel(BaseModel):

    SIZE = (
        ('A1' , 'A1'),
        ('A2' , 'A2'),
        ('A3' , 'A3'),
        ('A4' , 'A4'),
        ('Carta' , 'Carta'),
        ('Oficio', 'Oficio'),
    )

    TYPE_PRINT = (
        ('Offset', 'Offset'),
        ('Digital', 'Digital'),
    )

    TYPE_PAPER = (
        ('Couché', 'Couché'),
        ('Creativo', 'Creativo'),
        ('Offset', 'Offset'),
        ('Reciclado', 'Reciclado'),
        ('Autoadhesivo', 'Autoadhesivo'),
    )

    MEDIOS_COMUNICACION = (
        ('Zoom', 'Zoom'),
        ('WhatsApp', 'WhatsApp'),
        ('FB-messenger', 'FB-messenger'),
    )

    usuario                     = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True) 
    fecha_cita                  = models.DateTimeField('Fecha de la Cita:',auto_now=False, auto_now_add=False)
    size                        = models.CharField('Tamaño del papel:',max_length=50, choices=SIZE)
    type_print                  = models.CharField('Tipo de impresión:',max_length=50, choices=TYPE_PRINT)
    type_paper                  = models.CharField('Tipo de papel:',max_length=50, choices=TYPE_PAPER)
    medio_comunicacion          = models.CharField('Medio de Comunicación:',max_length=50, choices=MEDIOS_COMUNICACION)
    descripcion_complementaria  = RichTextField('Descripción Complementaria:',blank=True,)
    design                      = models.ForeignKey(Design, on_delete=models.CASCADE, blank=True, null=True)
    precio                      = models.DecimalField('Precio', max_digits=5, decimal_places=2,blank=True, null=True)
    pagado                      = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Solicitud Diseño + Impresión Papel'
        verbose_name_plural = 'Solicitudes Diseño + Impresión Papel'

    def __str__(self):
        return str(self.usuario)

class SolicitudDesignImpresionObjeto(BaseModel):

    MEDIOS_COMUNICACION = (
        ('Zoom', 'Zoom'),
        ('WhatsApp', 'WhatsApp'),
        ('FB-messenger', 'FB-messenger'),
    )

    usuario                     = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True) 
    fecha_cita                  = models.DateTimeField('Fecha de la Cita:',auto_now=False, auto_now_add=False)
    object_print                = models.CharField('Objeto a Imprimir:', max_length=1000)
    medio_comunicacion          = models.CharField('Medio de Comunicación:',max_length=50, choices=MEDIOS_COMUNICACION)
    descripcion_complementaria  = RichTextField('Descripción Complementaria:',blank=True,)
    design                      = models.ForeignKey(Design, on_delete=models.CASCADE, blank=True, null=True)
    precio                      = models.DecimalField('Precio', max_digits=5, decimal_places=2,blank=True, null=True)
    pagado                      = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Solicitud Diseño + Impresión Objeto'
        verbose_name_plural = 'Solicitudes Diseño + Impresión Objeto'

    def __str__(self):
        return str(self.usuario)

class SolicitudImpresionObjeto(BaseModel):

    MEDIOS_COMUNICACION = (
        ('Zoom', 'Zoom'),
        ('WhatsApp', 'WhatsApp'),
        ('FB-messenger', 'FB-messenger'),
    )

    usuario                     = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=True, null=True) 
    fecha_cita                  = models.DateTimeField('Fecha de la Cita:',auto_now=False, auto_now_add=False)
    object_print                = models.CharField('Objeto a Imprimir:', max_length=1000)
    medio_comunicacion          = models.CharField('Medio de Comunicación:',max_length=50, choices=MEDIOS_COMUNICACION)
    descripcion_complementaria  = RichTextField('Descripción Complementaria:',blank=True,)
    design                      = models.ForeignKey(Design, on_delete=models.CASCADE, blank=True, null=True) 
    precio                      = models.DecimalField('Precio', max_digits=5, decimal_places=2,blank=True, null=True)
    pagado                      = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Solicitud Impresión Objeto'
        verbose_name_plural = 'Solicitudes Impresión Objeto'

    def __str__(self):
        return str(self.usuario)