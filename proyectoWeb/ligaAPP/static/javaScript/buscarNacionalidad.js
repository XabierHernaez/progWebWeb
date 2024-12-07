document.addEventListener("DOMContentLoaded", function () {
    // Obtén el select de nacionalidades
    const nacionalidadSelect = document.getElementById('nacionalidadSelect');

    // Obtener todas las nacionalidades de los jugadores y eliminar duplicados
    const nacionalidades = new Set(); // Usamos un Set para eliminar duplicados

    // Recorrer todos los jugadores y agregar las nacionalidades al Set
    document.querySelectorAll('details p[data-nacionalidad]').forEach(jugadorP => {
      const nacionalidad = jugadorP.getAttribute('data-nacionalidad');
      
      // Verificar que la nacionalidad no esté vacía o sea null
      if (nacionalidad && nacionalidad.trim() !== '') {
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

    // Asegurarse de tener la opción "Todas" como primera opción
    const optionAll = document.createElement('option');
    optionAll.value = "";
    optionAll.textContent = "Todas";
    nacionalidadSelect.insertBefore(optionAll, nacionalidadSelect.firstChild); // Inserta "Todas" como primer opción

    // Función para actualizar la visibilidad de los jugadores según el filtro
    const updateJugadores = () => {
      const selectedNacionalidad = nacionalidadSelect.value; // Nacionalidad seleccionada

      // Recorrer todos los jugadores y filtrar según la nacionalidad seleccionada
      document.querySelectorAll('details p[data-nacionalidad]').forEach(jugadorP => {
        const jugadorNacionalidad = jugadorP.getAttribute('data-nacionalidad');

        // Filtra los jugadores por la nacionalidad seleccionada
        if (
          (selectedNacionalidad === "" || jugadorNacionalidad === selectedNacionalidad)
        ) {
          jugadorP.style.display = "block"; // Muestra el jugador
        } else {
          jugadorP.style.display = "none"; // Oculta el jugador
        }
      });
    };

    // Actualiza la visibilidad de los jugadores cuando cambia el filtro de nacionalidad
    nacionalidadSelect.addEventListener("change", updateJugadores);

    // Llama a la función una vez para ajustar la visibilidad al cargar la página
    updateJugadores();
  });