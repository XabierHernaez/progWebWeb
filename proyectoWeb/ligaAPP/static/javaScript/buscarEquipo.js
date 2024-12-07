document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("buscarEquipo"); // El campo de texto para buscar
    const equipoSidebar = document.querySelectorAll('.sidebar_item p'); // Los elementos de jugadores en la sidebar
    const equipoContenido = document.querySelectorAll('.equipoFormato'); // Los elementos de jugadores en el contenido principal

    // Función para actualizar los checkboxes y ocultar los jugadores según la nacionalidad
    searchInput.addEventListener("input", function() {
        const query = searchInput.value.toLowerCase(); // Convertir la entrada a minúsculas

        // Iterar sobre los jugadores en la sidebar
        equipoSidebar.forEach(function(equipo) {
            const nombreEquipo = equipo.getAttribute("data-nombre").toLowerCase(); // Obtener la nacionalidad del jugador
            const checkbox = equipo.querySelector('input[type="checkbox"]'); // El checkbox del equipo

            // Verificar si la nacionalidad coincide con la búsqueda
            if (nombreEquipo.includes(query)) {
                checkbox.checked = true; // Marcar el checkbox si coincide
            } else {
                checkbox.checked = false; // Desmarcar el checkbox si no coincide
            }
        });

        // Iterar sobre los jugadores en el contenido principal
        equipoContenido.forEach(function(equipo) {
            const nombreEquipo = equipo.getAttribute("data-nombre").toLowerCase(); // Obtener la nacionalidad del jugador
            const equipoElemento = equipo.closest('li'); // El <li> del jugador (para ocultarlo)

            // Verificar si la nacionalidad coincide con la búsqueda
            if (nombreEquipo.includes(query)) {
                equipoElemento.style.display = ''; // Mostrar el jugador si coincide
            } else {
                equipoElemento.style.display = 'none'; // Ocultar el jugador si no coincide
            }
        });
    });
});