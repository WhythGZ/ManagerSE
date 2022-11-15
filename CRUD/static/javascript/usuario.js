$(function() // public static void main (JAVa)
{
    $(".btnCreate").click(function()
    {
        let nombre = $(".txtNombre").val();
        let apellido = $(".txtApellido").val();
        let fecNac = $(".fecNac").val();
        let rut = $(".txtRut").val();
        let dv = $(".txtDV").val();
        let username = $(".txtUsername").val();
        let password1 = $(".txtPassword").val();
        let password2 = $(".txtPassword2").val();
        let email = $(".txtEmail").val();
        let direccion = $(".txtDireccion").val();
        let telefono = $(".txtTel").val();
        let rutInv = rut.split("").reverse().join("");
        let suma = 0;
        let rdv = '';
        let multiplicador = 2;
        let tipoDeUsuario = $(".cmbTipoUsuario").val();
        for (let i = 0; i<rutInv.length; i++){
            if (multiplicador == 7){
                suma += (rutInv[i] * parseInt(multiplicador));
                multiplicador = 2;
            }else{
                suma += (rutInv[i] * parseInt(multiplicador));
                multiplicador++;
            }
        }
        let mod = 11 - (suma%11)
        if(mod == 10){
            rdv = 'k';
        }
        else if (mod == 11){
            rdv = '0';
        }
        else {
            rdv = mod;
        }
        if(!rut)
        {
            alert("Debe especificar el Rut");
            $(".txtRut").focus();
        }           
        else if(!dv)
        {   
            if(!rut){
                alert("Debe especificar el Digito verificador");
                $(".txtDV").focus();
            }
            // else{
            //     $('.txtDV').val(rdv);
            // }
        }
        else if(!username){
            alert("Debe especificar el Nombre de usuario");
            $(".txtUsername").focus();
        }
        else if(!nombre)
        {
            alert("Debe especificar el Nombre");
            $(".txtNombre").focus();
        }
        else if(!apellido)
        {
            alert("Debe especificar el Apellido");
            $(".txtApellido").focus();
        }
        else if(!fecNac)
        {   
            alert("Debe especificar su Fecha de Nacimiento");
            $(".fecNac").focus();
        }
        else if(!password1)
        {
            alert("Debe especificar la contraseña");
            $(".txtPassword").focus();
        }    
        else if(password1.length<8)
        {
            alert("La contraseña debe tener como minimo 8 caracteres")
            $(".txtPassword").focus();
        }    
        else if(!password2)
        {
            alert("Debe confirmar la contraseña");
            $(".txtPassword2").focus();
        }    
        else if(password2.length<8)
        {
            alert("La contraseña debe tener como minimo 8 caracteres")
            $(".txtPassword").focus();
        }    
        else if(password1!=password2){
            alert("Las contraseñas deben coincidir");
            return false;
        }
        else if(!email){
            alert("Debe especificar el correo");
            $(".txtEmail").focus();
        }
        else if(email.length<8){
            alert("El correo debe tener como minimo 8 caracteres")
            $(".txtEmail").focus();
        }
        else if(email.indexOf('@', 0) == -1 || email.indexOf('.', 0) == -1) {
            alert('El correo electrónico introducido no es correcto.');
            return false;
        }
        else if(!direccion){
            alert("Debe especificar la direccion");
            $(".txtDireccion").focus();
        }
        else if(!telefono){
            alert("Debe especificar el telefono");
            $(".txtTelefono").focus();
        }
        else if(telefono.length<11){
            alert("El telefono debe tener como minimo 11 caracteres");
            $(".txtTelefono").focus();
        }
        else if(tipoDeUsuario == '0'){
            alert("Debe especificar el tipo de usuario");
            $(".cmbTipoUsuario").focus();
        }
        else{
            alert("Registrado correctamente");
        }
    });
    let correo = 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ@.1234567890_-';
    $(".txtEmail").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(correo.indexOf(caracter) < 0)
            return false;
    })
    let letras = 'qwertyu -iopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ';
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    $(".txtApellido").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
    let rut = '1234567890';
    $(".txtRut").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(rut.indexOf(caracter) < 0)
            return false;

    })
    let dv = '0123456789kK';
    $(".txtDV").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(dv.indexOf(caracter) < 0)
            return false;
    })
    let tel = '0123456789+';
    $(".txtTel").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(tel.indexOf(caracter) < 0)
            return false;
    })

});