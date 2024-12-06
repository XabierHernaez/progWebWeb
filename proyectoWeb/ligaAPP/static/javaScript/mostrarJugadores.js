// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function () {
    // Obtén todos los checkboxes
    const checkboxes = document.querySelectorAll('.sidebar_item input[type="checkbox"]');

    // Función para actualizar la visibilidad de los equipos
    const updateJugadores = () => {
        checkboxes.forEach(checkbox => {
            const jugadorId = checkbox.value; // El ID del equipo (asociado al checkbox)
            const jugadorDiv = document.querySelector(`#content .equipoFormato[data-jugador-id="${jugadorId}"]`);
            
            if (jugadorDiv) {
                if (checkbox.checked) {
                    jugadorDiv.style.display = "block"; // Muestra el equipo
                } else {
                    jugadorDiv.style.display = "none"; // Oculta el equipo
                }
            }
        });
    };

    // Asignar evento "change" a cada checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", updateJugadores);
    });

    // Llama una vez a la función para ajustar la visibilidad al cargar la página
    updateJugadores();
});