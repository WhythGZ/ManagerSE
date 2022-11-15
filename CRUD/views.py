from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Marca, Usuario
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

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
@permission_required('is_superuser')
def viewMarca(request):
    cntx = {}
    if request.method == 'POST':
        id = int("0" + request.POST["txtId"])
        nombreMarca = request.POST["txtNombre"]
        activo = False
        if 'chkActivo' in request.POST:
            activo = True
        if 'btnCreate' in request.POST:
            if len(nombreMarca) < 4:
                cntx = {'error': 'El nombre del tipo de usuario debe tener como minimo 5 caracteres'}
            elif id < 1:
                Marca.objects.create(nombreMarca = nombreMarca, activo = activo)
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
            else:
                fila = Marca.objects.get(pk = id)
                fila.nombreMarca = nombreMarca
                fila.activo = activo
                fila.save()
                cntx = {'mensaje': 'Los datos fueron guardados correctamente'}
        elif 'btnRead' in request.POST:
            listado = Marca.objects.all()
            if len(listado) >= 1:
                cntx = {'listado': listado }
            else:
                cntx = {'error': 'Aun no existen tipos de usuarios para mostrar'}
        elif 'btnDelete' in request.POST:
            try:
                fila = Marca.objects.get(pk = id)
                fila.delete()
                cntx = {'mensaje': 'Los datos fueron eliminados correctamente'}
            except:
                cntx = {'error': 'Debe seleccionar item a eliminar'}
    return render(request, 'marca.html', cntx)

@login_required
@permission_required('is_superuser')  
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
    return render(request, 'inicio.html', cntx)