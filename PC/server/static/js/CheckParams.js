document.addEventListener('DOMContentLoaded', function () {
    var formulario = document.getElementById('formulario');

    formulario.addEventListener('submit', function (event) {
        // Obtener todos los checkboxes con name="archivos"
        var checkboxes = document.getElementsByName('archivos');
        
        // Verificar si al menos uno está marcado
        var alMenosUnoMarcado = false;
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                alMenosUnoMarcado = true;
                break;
            }
        }

        // Si ninguno está marcado, mostrar un mensaje de error y detener el envío del formulario
        if (!alMenosUnoMarcado) {
            alert('Por favor, selecciona al menos una variable.');
            event.preventDefault(); // Detener el envío del formulario
        }
    });
});