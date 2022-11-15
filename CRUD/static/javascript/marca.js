$(function()
{
    $(".btnCreate").click(function()
    {
        let nombre = $(".txtNombre").val();
        if(!nombre){
            alert("Debe especificar el nombre de la marca");
            $(".txtNombre").focus();
            return false;
        }
        else if (nombre.length<4){
            alert("El nombre de la marca debe tener como minimo 5 caracteres");
            $(".txtNombre").focus();
            return false;
        }
        else{
            alert("Marca registrada correctamente");
        }
    });
    let letras = "qwertyuiopasdfghjklzxcvbnm- ñQWERTYUIOPASDFGHJKLZXCVBNMÑ1234567890'";
    $(".txtNombre").keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)
            return false;

    })
});