$(function() // public static void main (JAVa)
{
    $(".btnEnviar").click(function()
    {
        let Username = $(".id_username").val();
        let Password = $(".id_password").val();

        if(!Username)
        {
            alert("Debe especificar el nombre de usuario");
            $(".id_username").focus();
        }     
        else if(Username.length<4){
            alert("El nombre de usuario debe tener como minimo 4 caracteres")
            $(".id_username").focus();
        }    
        else if(!Password)
        {
            alert("Debe especificar la contraseña");
            $(".id_password").focus();
        }
        else if(Password.length<8)
        {
            alert("La contraseña debe tener como minimo 8 caracteres")
            $(".id_password").focus();
        }
    });
    let letras = 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNMÑ';
    $(".id_username").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;
    })
});