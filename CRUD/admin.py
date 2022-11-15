from django.contrib import admin
from .models import Usuario, Marca
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Marca)
admin.site.register(Usuario, UserAdmin)