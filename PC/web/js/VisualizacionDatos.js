document.getElementById("csvForm").addEventListener("submit", function (event) {
    event.preventDefault();
    var formData = new FormData(this);

    // Realizar la solicitud POST con AJAX
    fetch('http://localhost:5000/visualizar_datos', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            // Verificar si la respuesta contiene la ruta completa
            if (data.plot_html) {
                // Abrir una nueva ventana con la ruta completa del gráfico HTML
                window.open(data.plot_html, '_blank');
            } else {
                console.error('La respuesta no contiene la ruta del gráfico HTML.');
            }
        })
        .catch(error => {
            console.error('Error al procesar la solicitud:', error);
        });
});