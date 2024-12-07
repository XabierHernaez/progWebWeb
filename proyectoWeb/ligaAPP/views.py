from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Liga, Equipo, Jugador
import requests
from bs4 import BeautifulSoup


def obtener_datos(request):
    # URL de la página web a analizar
    url = 'https://www.marca.com/'
    
    # Realizamos una solicitud GET para obtener el contenido de la página
    response = requests.get(url)
    
    if response.status_code == 200:
        # Usamos BeautifulSoup con el parser lxml
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Extraemos un elemento (por ejemplo, el título de la página)
        titulo = soup.title.string
        
        # Devolvemos el título en una respuesta HTTP
        return HttpResponse(f'El título de la página es: {titulo}')
    else:
        return HttpResponse('Error al obtener la página', status=500)

class IndexView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return None  

class listaLigas(ListView):
    model= Liga
    template_name= 'listaLigas.html'
    context_object_name = 'listaLigas'
    queryset = Liga.objects.order_by('-nombre')

class listaEquipos(ListView):
    model= Equipo
    template_name= 'listaEquipos.html'
    context_object_name = 'listaEquipos'
    queryset = Equipo.objects.order_by('-nombre')

class listaJugadores(ListView):
    model = Jugador
    template_name = 'listaJugadores.html'
    context_object_name = 'listaJugadores'
    queryset = Jugador.objects.order_by('-nombre')

class DetalleLigaView(DetailView):
    model = Liga
    template_name = 'detalleLiga.html'
    context_object_name = 'detalleLiga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipos'] = self.object.equipos.all()  # Acceso correcto
        return context

class DetalleEquipoView(DetailView):
    model = Equipo
    template_name = 'detalleEquipo.html'
    context_object_name = 'detalleEquipo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jugadores'] = self.object.jugadores.all()  
        return context

class DetalleJugadorView(DetailView):
    model = Jugador
    template_name = 'detalleJugador.html'
    context_object_name = 'detalleJugador'