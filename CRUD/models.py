from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os
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
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.rut


class Marca(models.Model):
    nombreMarca = models.TextField(max_length=50)
    activo = models.BooleanField()
    imgMarca = models.ImageField(upload_to = "marca", null = True)
    def __str__(self):
        return self.nombreMarca


class Vehiculo(models.Model):
    idCliente = models.IntegerField()
    patente = models.CharField(max_length= 6, unique = True)
    padron = models.CharField(max_length=17, unique = True)
    color  = models.CharField(max_length = 15)
    modelo = models.CharField(max_length = 20)
    marca = models.TextField(max_length=50)
    year = models.IntegerField()

class Cita(models.Model):
    idCliente = models.IntegerField()
    idVehiculo = models.IntegerField()
    fechaCita = models.DateField()
    horaCita = models.TimeField()
