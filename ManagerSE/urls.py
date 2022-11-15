from django.contrib import admin
from django.urls import path, include
from CRUD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', views.viewCliente, name="signin"),
    path('login', views.viewLogin, name="login"),
    path('reset', views.viewReset, name="reset"),
    path('', views.viewInicio, name="inicio"),
    path('crud/', include('CRUD.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
