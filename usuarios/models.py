from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager 

# Create your models here.

class Usuarios(AbstractBaseUser, PermissionsMixin):

    username    = models.CharField(max_length=30, unique=True)
    email       = models.EmailField(max_length=254, unique=True)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    codregistro = models.CharField(max_length=10, blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name