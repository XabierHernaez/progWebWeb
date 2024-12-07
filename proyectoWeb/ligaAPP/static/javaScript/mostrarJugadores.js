document.addEventListener("DOMContentLoaded", function () {
    // Obtén todos los checkboxes y el select de nacionalidades
    const checkboxes = document.querySelectorAll('details input[type="checkbox"]');
    const nacionalidadSelect = document.getElementById('nacionalidadSelect');
    
    // Obtener todas las nacionalidades de los jugadores y eliminar duplicados
    const nacionalidades = new Set(); // Usamos un Set para eliminar duplicados
    
    // Recorrer todos los jugadores y agregar las nacionalidades al Set
    document.querySelectorAll('details p[data-nacionalidad]').forEach(jugadorP => {
      const nacionalidad = jugadorP.getAttribute('data-nacionalidad');
      if (nacionalidad) {
        nacionalidades.add(nacionalidad);
      }
    });
  
    // Crear las opciones del select con las nacionalidades únicas
    nacionalidades.forEach(nacionalidad => {
      const option = document.createElement('option');
      option.value = nacionalidad;
      option.textContent = nacionalidad;
      nacionalidadSelect.appendChild(option);
    });
  
    // Función para actualizar la visibilidad de los jugadores
    const updateJugadores = () => {
      const selectedNacionalidad = nacionalidadSelect.value; // Nacionalidad seleccionada
    
      checkboxes.forEach(checkbox => {
        const jugadorP = checkbox.closest('p'); // Encuentra el elemento <p> que contiene el jugador
        const jugadorNacionalidad = jugadorP.getAttribute('data-nacionalidad');
    
        // Filtra por nacionalidad y checkbox
        if (
          (selectedNacionalidad === "" || jugadorNacionalidad === selectedNacionalidad) &&
          checkbox.checked
        ) {
          jugadorP.style.display = "block"; // Muestra el jugador
        } else {
          jugadorP.style.display = "none"; // Oculta el jugador
        }
      });
    };
    
    // Actualiza cuando cambian los checkboxes
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener("change", updateJugadores);
    });
    
    // Actualiza cuando cambia el filtro de nacionalidad
    nacionalidadSelect.addEventListener("change", updateJugadores);
    
    // Llama una vez a la función para ajustar la visibilidad al cargar la página
    updateJugadores();
  });
  