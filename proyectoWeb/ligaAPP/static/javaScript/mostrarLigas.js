// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function () {
    // Obtén todos los checkboxes dentro del <details>
    const checkboxes = document.querySelectorAll('details input[type="checkbox"]');
  
    // Función para actualizar la visibilidad de las ligas
    const updateLigas = () => {
      checkboxes.forEach(checkbox => {
        const ligaId = checkbox.value; // El ID del equipo (asociado al checkbox)
        const ligaDiv = document.querySelector(`#content .equipoFormato[data-liga-id="${ligaId}"]`);
        
        if (ligaDiv) {
          // Muestra u oculta el equipo según el estado del checkbox
          ligaDiv.style.display = checkbox.checked ? "block" : "none";
        }
      });
    };
  
    // Asigna el evento "change" a cada checkbox para que actualice la visibilidad
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener("change", updateLigas);
    });
  
    // Llama una vez a la función para ajustar la visibilidad al cargar la página
    updateLigas();
  });
