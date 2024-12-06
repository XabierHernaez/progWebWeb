// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function () {
    // Obtén todos los checkboxes
    const checkboxes = document.querySelectorAll('.sidebar_item input[type="checkbox"]');

    // Función para actualizar la visibilidad de los equipos
    const updateEquipos = () => {
        checkboxes.forEach(checkbox => {
            const equipoId = checkbox.value; // El ID del equipo (asociado al checkbox)
            const equipoDiv = document.querySelector(`#content .equipoFormato[data-equipo-id="${equipoId}"]`);
            
            if (equipoDiv) {
                if (checkbox.checked) {
                    equipoDiv.style.display = "block"; // Muestra el equipo
                } else {
                    equipoDiv.style.display = "none"; // Oculta el equipo
                }
            }
        });
    };

    // Asignar evento "change" a cada checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", updateEquipos);
    });

    // Llama una vez a la función para ajustar la visibilidad al cargar la página
    updateEquipos();
});