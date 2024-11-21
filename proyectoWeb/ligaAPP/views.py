from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Liga, Equipo, Jugador

def index(request):
    return render(request, 'index.html')

def listaLigas(request):
    ligas = Liga.objects.order_by('nombre')
    contexto = {'liga_list': ligas}
    return render(request, 'listaLigas.html', contexto)

#class ListaTrabajadorViuw(ListaViuw):
    #model = trabajador
    #template_name= 'detalle.html!
    #context_object_name = 'lista_trabakadores'
    

def listaEquipos(request):
    equipos = Equipo.objects.order_by('nombre')
    contexto = {'equipo_list': equipos}
    return render(request, 'listaEquipos.html', contexto)

def listaJugadores(request):
    jugadores = Jugador.objects.order_by('nombre')
    contexto = {'jugador_list': jugadores}
    return render(request, 'listaJugadores.html', contexto)

def detalleLiga(request, id_liga):
    liga = get_object_or_404(Liga, pk=id_liga)
    equipos = liga.equipos.all()
    contexto = {'liga': liga, 'equipos': equipos}
    return render(request, 'detalleLiga.html', contexto)

def detalleEquipo(request, id_equipo):
    equipo = get_object_or_404(Equipo, pk=id_equipo)
    jugadores = equipo.jugadores.all()
    contexto = {'equipo': equipo, 'jugadores': jugadores}
    return render(request, 'detalleEquipo.html', contexto)

def detalleJugador(request, id_jugador):
    jugador = get_object_or_404(Jugador, pk=id_jugador)
    contexto = {'jugador': jugador}
    return render(request, 'detalleJugador.html', contexto)