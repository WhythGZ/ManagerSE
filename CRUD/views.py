from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Cita, Marca, Servicios, Usuario, Vehiculo
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@login_required
@permission_required('is_superuser')
def viewUsuario(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        rut = request.POST["txtRut"]
        dv = request.POST["txtDV"]
        username = request.POST["txtUsername"]
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"] 

        fechaNac = request.POST["fecNac"]
        raw_password = request.POST["txtPassword"]
        password = make_password(raw_password, salt=None, hasher='default')
        email = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        telefono = request.POST["txtTel"]
        tipoDeUsuario = request.POST["cmbTipoUsuario"]
        if (tipoDeUsuario == '3'):
            is_super = True
            is_staff = True
        elif (tipoDeUsuario == '2'):
            is_super = False
            is_staff = True
        else:
            is_super = False
            is_staff = False
        if 'btnCreate' in request.POST:
            if len(rut)<8:
                cntx = {'error': 'El rut del usuario debe tener como minimo 8 caracteres'}
            elif len(dv)<1:
                cntx = {'error': 'Debe especificar el digito verificador'}
            elif len(username) < 3:
                cntx = {'error': 'El nombre de usuario debe tener como minimo 3 caracteres'}
            elif len(nombre) < 3:
                cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(apellido) < 3:
                cntx = {'error': 'El apellido del usuario debe tener como minimo 3 caracteres'}
            # elif len(fechaNac) < 3: 
            #     cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(raw_password) < 8:
                cntx = {'error': 'La contraseña del usuario debe tener como minimo 8 caracteres'}
            elif len(email) < 8:
                cntx = {'error': 'El correo del usuario debe tener como minimo 8 caracteres'}
            elif len(direccion) < 8:
                cntx = {'error': 'La direccion del usuario debe tener como minimo 8 caracteres'}
            elif len(telefono) < 8:
                cntx = {'error': 'El telefono del usuario debe tener como minimo 8 caracteres'}
            elif tipoDeUsuario == '0':
                cntx = {'error': 'Debe seleccionar un tipo de usuario'}
            elif id < 1:
                Usuario.objects.create(rut = rut , dv = dv, username = username, first_name = nombre, last_name = apellido, fechaNac = fechaNac, password = password, email = email, direccion = direccion, telefono = telefono, is_superuser = is_super, is_staff = is_staff)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Usuario.objects.get(pk = id)
                fila.rut = rut
                fila.dv = dv
                fila.username = username
                fila.first_name = nombre
                fila.last_name = apellido
                fila.fechaNac = fechaNac
                fila.password = password
                fila.email = email
                fila.direccion = direccion
                fila.telefono = telefono
                fila.tipoDeUsuario = tipoDeUsuario
                fila.is_superuser = is_super
                fila.is_staff = is_staff
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Usuario.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen usuarios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Usuario.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    return render(request, 'usuario.html', cntx)

@login_required
@permission_required('is_superuser')  
def viewReadUsuario(request, id):
    cntx = {}
    try:
        fila = Usuario.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    return render(request, 'usuario.html', cntx)

@login_required
@staff_member_required
def viewMarca(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreMarca = request.POST["txtNombre"]
        imgMarca = request.POST["formFile"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreMarca) < 4:
                cntx = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            elif len(imgMarca)<1:
                cntx = {'error': 'Debe seleccionar una imagen'}
            elif id < 1:
                Marca.objects.create(nombreMarca = nombreMarca, activo = activo, imgMarca = imgMarca)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}  
            else:
                fila = Marca.objects.get(pk = id)
                fila.nombreMarca = nombreMarca
                fila.activo = activo
                fila.imgMarca = imgMarca
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Marca.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen marcas para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Marca.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    return render(request, 'marca.html', cntx)

@login_required
@staff_member_required
def viewReadMarca(request, id):
    cntx = {}
    try:
        fila = Marca.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    return render(request, 'marca.html', cntx)

def viewCliente(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        rut = request.POST["txtRut"]
        dv = request.POST["txtDV"]
        username = request.POST["txtUsername"]
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"]
        fechaNac = request.POST["fecNac"]
        raw_password = request.POST["txtPassword"]
        password = make_password(raw_password, salt=None, hasher='default')
        email = request.POST["txtEmail"]
        direccion = request.POST["txtDireccion"]
        telefono = request.POST["txtTel"]
        if 'btnCreate' in request.POST:
            if len(rut)<8:
                cntx = {'error': 'El rut del usuario debe tener como minimo 8 caracteres'}
            elif len(dv)<1:
                cntx = {'error': 'Debe especificar el digito verificador'}
            elif len(nombre) < 3:
                cntx = {'error': 'El nombre del usuario debe tener como minimo 3 caracteres'}
            elif len(apellido) < 3:
                cntx = {'error': 'El apellido del usuario debe tener como minimo 3 caracteres'}
            elif len(password) < 8:
                cntx = {'error': 'La contraseña del usuario debe tener como minimo 8 caracteres'}
            elif len(email) < 8:
                cntx = {'error': 'El correo del usuario debe tener como minimo 8 caracteres'}
            elif len(direccion) < 8:
                cntx = {'error': 'La direccion del usuario debe tener como minimo 8 caracteres'}
            elif len(telefono) < 8:
                cntx = {'error': 'El telefono del usuario debe tener como minimo 8 caracteres'}
            elif id < 1:
                Usuario.objects.create(rut = rut , dv = dv, username = username, first_name = nombre, last_name = apellido, fechaNac = fechaNac, password = password, email = email, direccion = direccion, telefono = telefono)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Usuario.objects.get(pk = id)
                fila.rut = rut
                fila.dv = dv
                fila.username = username
                fila.nombre = nombre
                fila.apellido = apellido
                fila.fechaNac = fechaNac
                fila.password = password
                fila.email = email
                fila.direccion = direccion
                fila.telefono = telefono
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        
    return render(request, 'cliente.html', cntx)

def viewLogin(request):
    cntx = {}
    return render(request, 'login.html', cntx)

def viewReset(request):
    cntx = {}
    return render(request, 'reset.html', cntx)

def viewInicio(request):
    cntx = {}
    services = Servicios.objects.all()
    brands = Marca.objects.all()
    cntx["services"] = services
    cntx["brands"] = brands
    return render(request, 'inicio.html', cntx)

@login_required
def viewVehiculo(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        idCliente = int(request.POST["user_id"])
        patente = request.POST["txtPatente"]
        padron = request.POST["txtPadron"]
        color = request.POST["txtColor"]
        modelo = request.POST["txtModelo"]
        marca = request.POST["txtMarca"]
        year = request.POST["txtAnio"]
        if 'btnCreate' in request.POST:
            if len(patente)<6:
                cntx = {'error': 'La patente del auto debe tener como minimo 6 caracteres'}
            elif len(padron)<15:
                cntx = {'error': 'El padron del vehiculo debe tener como minimo 15 caracteres'}
            elif len(color) < 0:
                cntx = {'error': 'El color del auto debe especificarse'}
            elif len(modelo) < 1:
                cntx = {'error': 'El modelo del auto debe tener como minimo 10 caracteres'}
            elif marca == "0":
                cntx = {'error': 'La marca del vehiculo debe ser especificada'}
            elif len(year) < 4:
                cntx = {'error': 'El año del auto debe tener como minimo 4 caracteres'}
            elif id < 1:
                Vehiculo.objects.create(idCliente = idCliente, patente = patente , padron = padron, color = color, modelo = modelo, marca= marca, year = year)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Vehiculo.objects.get(pk = id)
                fila.idCliente = idCliente
                fila.patente = patente
                fila.padron = padron
                fila.color = color
                fila.modelo = modelo
                fila.marca = marca
                fila.year = year
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Vehiculo.objects.filter(idCliente=idCliente)
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen vehiculos para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Vehiculo.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    marcas = Marca.objects.all()
    cntx["marcas"] = marcas
    return render(request, 'vehiculo.html', cntx)

@login_required
def viewReadVehiculo(request, id):
    cntx = {}
    try:
        fila = Vehiculo.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    marcas = Marca.objects.all()
    cntx["marcas"] = marcas
    return render(request, 'vehiculo.html', cntx)

@login_required
def viewCita(request):
    cntx = {}
    user = request.user
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        idCliente = request.POST["txtIdCliente"]
        idVehiculo = request.POST["cmbVehiculo"]
        idServicio = request.POST["cmbServicio"]
        try:
            estado = request.POST["cmbEstado"]
            fechaCita = request.POST["fecCita"]
            horaCita = request.POST["horaCita"]
        except:
            estado = 1
            fechaCita = "0001-01-01"
            horaCita = "00:00"
        if 'btnCreate' in request.POST:
            if idVehiculo == 0 :
                cntx = {'error': 'Debe especificar el vehiculo'}
            elif id < 1:
                Cita.objects.create(idCliente = idCliente, idVehiculo = idVehiculo, fechaCita = fechaCita, horaCita = horaCita, estado = estado, idServicio = idServicio)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}  
            else:
                fila = Cita.objects.get(pk = id)
                fila.idCliente = idCliente 
                fila.idVehiculo = idVehiculo 
                fila.fechaCita = fechaCita 
                fila.horaCita = horaCita
                fila.estado = estado
                fila.idServicio = idServicio
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Cita.objects.filter(idCliente=idCliente)
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen citas para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Cita.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    userVehicles = Vehiculo.objects.filter(idCliente=user.id)
    cntx["userVehicles"] = userVehicles
    services = Servicios.objects.all()
    cntx["services"] = services
    return render(request, 'agendar.html', cntx)

@login_required
def viewReadCita(request, id, clientId):
    cntx = {}
    try:
        fila = Cita.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    userVehicles = Vehiculo.objects.filter(idCliente=clientId)
    cntx["userVehicles"] = userVehicles
    services = Servicios.objects.all()
    cntx["services"] = services
    return render(request, 'agendar.html', cntx)

@login_required
@staff_member_required
def viewCitaStaff(request):
    cntx = {}
    listado = Cita.objects.all()
    if len(listado) >= 1:
        cntx = {'listado': listado }
    else:
        cntx = {'error': 'Aun no existen citas para mostrar'}
    services = Servicios.objects.all()
    cntx["services"] = services
    vehicles = Vehiculo.objects.all()
    cntx["vehicles"] = vehicles
    users = Usuario.objects.all()
    cntx["users"] = users
    return render(request, 'citas.html', cntx)

@login_required
@staff_member_required
def viewReadCitaStaff(request, id, idVehicle, idService):
    cntx = {}
    user = request.user
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        idCliente = request.POST["txtIdCliente"]
        idVehiculo = idVehicle
        idServicio = idService
        estado = request.POST["cmbEstado"]
        fechaCita = request.POST["fecCita"]
        horaCita = request.POST["horaCita"]
        if 'btnCreate' in request.POST:
            if idVehiculo == 0 :
                cntx = {'error': 'Debe especificar el vehiculo'}
            elif id < 1:
                Cita.objects.create(idCliente = idCliente, idVehiculo = idVehiculo, fechaCita = fechaCita, horaCita = horaCita, estado = estado, idServicio = idServicio)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}  
            else:
                fila = Cita.objects.get(pk = id)
                fila.idCliente = idCliente 
                fila.idVehiculo = idVehiculo 
                fila.idServicio = idServicio
                fila.fechaCita = fechaCita 
                fila.horaCita = horaCita
                fila.estado = estado
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Cita.objects.filter(idCliente=idCliente)
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen citas para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Cita.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    userVehicles = Vehiculo.objects.filter(idCliente=user.id)
    cntx["userVehicles"] = userVehicles
    services = Servicios.objects.all()
    cntx["services"] = services
    return render(request, 'agendar.html', cntx)

def viewMarcas(request):
    cntx = {}
    marcas = Marca.objects.all()
    cntx["marcas"] = marcas
    return render(request, 'marcas.html', cntx)

@login_required
@staff_member_required
def viewServicios(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreServicio = request.POST["txtNombreServicio"]
        precioServicio = request.POST["txtPrecio"]
        descripcion = request.POST["txtDescripcion"]
        imgServicio = request.POST["formFile"]
        tiempo = request.POST["txtTiempo"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreServicio)<8:
                cntx = {'error': 'El nombre del servicio debe tener como minimo 8 caracteres'}
            elif len(precioServicio) == 0:
                cntx = {'error': 'El precio del servicio debe tener un valor'} 
            elif len(descripcion) < 10:
                cntx = {'error': 'La descripcion del servicio debe tener como minimo 10 caracteres'}
            elif len(tiempo) == 0 :
                cntx = {'error': 'El tiempo estimado debe tener un valor'}
            elif id < 1:
                Servicios.objects.create(nombreServicio = nombreServicio, precioServicio = precioServicio , descripcion = descripcion, tiempo = tiempo, activo = activo, imgServicio = imgServicio)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Servicios.objects.get(pk = id)
                fila.nombreServicio = nombreServicio
                fila.precioServicio = precioServicio
                fila.descripcion = descripcion
                fila.tiempo = tiempo
                fila.imgServicio = imgServicio
                fila.activo =activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Servicios.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen servicios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Servicios.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    servicios = Servicios.objects.all()
    cntx["servicios"] = servicios   
    return render(request, 'servicios.html',cntx)   


@login_required
@staff_member_required
def viewReadServicios(request,id):
    cntx = {}
    try:
        fila = Servicios.objects.get(pk = id)
        cntx = {'fila': fila}
    except:
        cntx = {'error': 'Item no encontrado'}
    servicios = Servicios.objects.all()
    cntx["servicios"] = servicios
    return render(request, 'servicios.html', cntx)