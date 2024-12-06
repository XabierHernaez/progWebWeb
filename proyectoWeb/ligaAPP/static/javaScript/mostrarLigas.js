// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function () {
    // Obtén todos los checkboxes
    const checkboxes = document.querySelectorAll('.sidebar_item input[type="checkbox"]');

    // Función para actualizar la visibilidad de los equipos
    const updateLigas = () => {
        checkboxes.forEach(checkbox => {
            const ligaId = checkbox.value; // El ID del equipo (asociado al checkbox)
            const ligaDiv = document.querySelector(`#content .equipoFormato[data-liga-id="${ligaId}"]`);
            
            if (ligaDiv) {
                if (checkbox.checked) {
                    ligaDiv.style.display = "block"; // Muestra el equipo
                } else {
                    ligaDiv.style.display = "none"; // Oculta el equipo
                }
            }
        });
    };

    // Asignar evento "change" a cada checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", updateLigas);
    });

    // Llama una vez a la función para ajustar la visibilidad al cargar la página
    updateLigas();
});