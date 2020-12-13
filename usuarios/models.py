from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager 

# Create your models here.

class Usuarios(AbstractBaseUser, PermissionsMixin):

    username        = models.CharField(max_length=30, unique=True)
    email           = models.EmailField(max_length=254, unique=True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    codregistro     = models.CharField(max_length=10, blank=True, null=True)
    monto_pagar     = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    confirmado      = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name
