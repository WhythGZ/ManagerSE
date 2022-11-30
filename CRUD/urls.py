from django.urls import path
from . import views
urlpatterns = [
    path('marca', views.viewMarca, name="marca"),
    path('marca/<int:id>/', views.viewReadMarca, name="marca"),
    path('usuario', views.viewUsuario, name="usuario"),
    path('usuario/<int:id>/', views.viewReadUsuario, name="usuario"),
    path('vehiculo', views.viewVehiculo, name="vehiculo"),
    path('vehiculo/<int:id>/', views.viewReadVehiculo, name="vehiculo"),
    path('cita', views.viewCita, name="cita"),
    path('cita/<int:id>/<int:clientId>/', views.viewReadCita, name="cita"),
    path('citas', views.viewCitaStaff, name="citas"),
    ]
