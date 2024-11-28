from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Liga, Equipo, Jugador

class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return None  

#def listaLigas(request):
 #   ligas = Liga.objects.order_by('nombre')
  #  contexto = {'liga_list': ligas}
   # return render(request, 'listaLigas.html', contexto)

class listaLigas(ListView):
    model= Liga
    template_name= 'listaLigas.html'
    context_object_name = 'listaLigas'
    queryset = Liga.objects.order_by('-nombre')

#class ListaTrabajadorViuw(ListaViuw):
    #model = trabajador
    #template_name= 'detalle.html!
    #context_object_name = 'lista_trabajadores'

#def listaEquipos(request):
 #   equipos = Equipo.objects.order_by('nombre')
  #  contexto = {'equipo_list': equipos}
   # return render(request, 'listaEquipos.html', contexto)

class listaEquipos(ListView):
    model= Equipo
    template_name= 'listaEquipos.html'
    context_object_name = 'listaEquipos'
    queryset = Equipo.objects.order_by('-nombre')


#def listaJugadores(request):
 #   jugadores = Jugador.objects.order_by('nombre')
  #  contexto = {'jugador_list': jugadores}
   # return render(request, 'listaJugadores.html', contexto)

class listaJugadores(ListView):
    model = Jugador
    template_name = 'listaJugadores.html'
    context_object_name = 'listaJugadores'
    queryset = Jugador.objects.order_by('-nombre')


#def detalleLiga(request, id_liga):
 #   liga = get_object_or_404(Liga, pk=id_liga)
  #  equipos = liga.equipos.all()
   # contexto = {'liga': liga, 'equipos': equipos}
    #return render(request, 'detalleLiga.html', contexto)

class DetalleLigaView(DetailView):
    model = Liga
    template_name = 'detalleLiga.html'
    context_object_name = 'detalleLiga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos'] = self.object.equipos.all()  # Acceso correcto
        return context

#def detalleEquipo(request, id_equipo):
 #   equipo = get_object_or_404(Equipo, pk=id_equipo)
  #  jugadores = equipo.jugadores.all()
   # contexto = {'equipo': equipo, 'jugadores': jugadores}
    #return render(request, 'detalleEquipo.html', contexto)

class DetalleEquipoView(DetailView):
    model = Equipo
    template_name = 'detalleEquipo.html'
    context_object_name = 'detalleEquipo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jugadores'] = self.object.jugadores.all()  
        return context


#def detalleJugador(request, id_jugador):
 #   jugador = get_object_or_404(Jugador, pk=id_jugador)
  #  contexto = {'jugador': jugador}
   # return render(request, 'detalleJugador.html', contexto)

class DetalleJugadorView(DetailView):
    model = Jugador
    template_name = 'detalleJugador.html'
    context_object_name = 'detalleJugador'