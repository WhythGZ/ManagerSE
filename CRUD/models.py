from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Usuario(AbstractUser):
    rut = models.TextField(max_length=10)
    dv = models.TextField(max_length=1)
    username = models.TextField(max_length=20, unique=True)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    fechaNac = models.DateField(null=True)
    password = models.CharField(max_length=128)
    email = models.TextField(max_length=30)
    direccion = models.TextField(max_length=30)
    telefono = models.TextField(max_length=12)
    last_login = models.DateField(default=timezone.now)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.rut

class Marca(models.Model):
    nombreMarca = models.TextField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombreMarca