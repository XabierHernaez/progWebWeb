document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("buscarJugadores"); // El campo de texto para buscar
    const jugadoresSidebar = document.querySelectorAll('.sidebar_item p'); // Los elementos de jugadores en la sidebar
    const jugadoresContenido = document.querySelectorAll('.equipoFormato'); // Los elementos de jugadores en el contenido principal

    // Función para actualizar los checkboxes y ocultar los jugadores según la nacionalidad
    searchInput.addEventListener("input", function() {
        const query = searchInput.value.toLowerCase(); // Convertir la entrada a minúsculas

        // Iterar sobre los jugadores en la sidebar
        jugadoresSidebar.forEach(function(jugador) {
            const nacionalidadJugador = jugador.getAttribute("data-nacionalidad").toLowerCase(); // Obtener la nacionalidad del jugador
            const checkbox = jugador.querySelector('input[type="checkbox"]'); // El checkbox del jugador

            // Verificar si la nacionalidad coincide con la búsqueda
            if (nacionalidadJugador.includes(query)) {
                checkbox.checked = true; // Marcar el checkbox si coincide
            } else {
                checkbox.checked = false; // Desmarcar el checkbox si no coincide
            }
        });

        // Iterar sobre los jugadores en el contenido principal
        jugadoresContenido.forEach(function(jugador) {
            const nacionalidadJugador = jugador.getAttribute("data-nacionalidad").toLowerCase(); // Obtener la nacionalidad del jugador
            const jugadorElemento = jugador.closest('li'); // El <li> del jugador (para ocultarlo)

            // Verificar si la nacionalidad coincide con la búsqueda
            if (nacionalidadJugador.includes(query)) {
                jugadorElemento.style.display = ''; // Mostrar el jugador si coincide
            } else {
                jugadorElemento.style.display = 'none'; // Ocultar el jugador si no coincide
            }
        });
    });
});