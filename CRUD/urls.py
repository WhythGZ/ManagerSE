from django.urls import path
from . import views
urlpatterns = [
    path('marca', views.viewMarca, name="marca"),
    path('marca/<int:id>/', views.viewReadMarca, name="marca"),
    path('usuario', views.viewUsuario, name="usuario"),
    path('usuario/<int:id>/', views.viewReadUsuario, name="usuario"),
    ]