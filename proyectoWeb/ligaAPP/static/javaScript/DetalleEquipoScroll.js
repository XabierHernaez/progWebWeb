document.addEventListener("DOMContentLoaded", function() {
    // Seleccionamos el contenedor de jugadores
    const jugadoresContainer = document.getElementById('jugadores-container');
  
    // Detectamos el scroll y agregamos o quitamos la clase 'scroll-active'
    jugadoresContainer.addEventListener('scroll', function() {
      if (jugadoresContainer.scrollLeft > 0) {
        jugadoresContainer.classList.add('scroll-active');
      } else {
        jugadoresContainer.classList.remove('scroll-active');
      }
    });
  });
  