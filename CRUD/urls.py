from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('marca', views.viewMarca, name="marca"),
    path('marca/<int:id>/', views.viewReadMarca, name="marca"),
    path('usuario', views.viewUsuario, name="usuario"),
    path('usuario/<int:id>/', views.viewReadUsuario, name="usuario"),
    path('vehiculo', views.viewVehiculo, name="vehiculo"),
    path('vehiculo/<int:id>/', views.viewReadVehiculo, name="vehiculo"),
    path('cita', views.viewCita, name="cita"),
    path('cita/<int:id>/<int:clientId>/', views.viewReadCita, name="cita"),
    path('citas', views.viewCitas, name="citas"),
    path('citaM/<int:id>/<int:idVehicleP>/<int:idServiceP>/<int:idClienteP>/', views.viewCitaStaff, name='citaM'),
    path('marcas', views.viewMarcas, name="marcas"),
    path('servicios', views.viewServicios, name="servicios"),
    path('servicios/<int:id>/', views.viewReadServicios, name="servicios"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)