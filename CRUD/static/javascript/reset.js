$(function() // public static void main (JAVa)
{
    $(".btnEnviar").click(function()
    {
        let Email = $(".txtEmail").val();
        if(!Email)
        {
            alert("Debe especificar el correo");
            $(".txtEmail").focus();
        }
        else if(Email.length<8){
            alert("El correo debe tener como minimo 8 caracteres")
            $(".txtEmail").focus();
        }   
        else if(Email.indexOf('@', 0) == -1 || Email.indexOf('.', 0) == -1) {
            alert('El correo electrónico introducido no es correcto.');
            return false;
        }
        else{
            alert("Correo enviado correctamente...");
        }
    });
    let correo = 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ@.1234567890_-';
    $(".txtEmail").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(correo.indexOf(caracter) < 0)
            return false;
    })
});