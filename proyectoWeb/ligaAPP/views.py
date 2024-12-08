from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Liga, Equipo, Jugador
import requests
from bs4 import BeautifulSoup
import time


def obtener_datos(request):
    url = 'https://www.marca.com/futbol.html?intcmp=MENUPROD&s_kw=futbol'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        enlaces = soup.find_all('a', href=True)
        noticias = []

        for enlace in enlaces:
            if '/futbol/' in enlace['href']:
                enlace_noticia = enlace['href']
                if enlace_noticia.startswith('/'):
                    enlace_noticia = f'https://www.marca.com{enlace_noticia}'

                response_noticia = requests.get(enlace_noticia)
                if response_noticia.status_code == 200:
                    soup_noticia = BeautifulSoup(response_noticia.text, 'lxml')
                    titulo_noticia = soup_noticia.find('h1').get_text(strip=True) if soup_noticia.find('h1') else 'Título no disponible'
                    contenido_noticia = soup_noticia.find('div', {'class': 'ue-c-article__body'})
                    contenido_noticia = contenido_noticia.get_text(' ', strip=True) if contenido_noticia else 'Contenido no disponible'

                    noticias.append({
                        'titulo': titulo_noticia,
                        'contenido': contenido_noticia,
                        'enlace': enlace_noticia
                    })

                if len(noticias) >= 3:
                    break

        return render(request, 'marca.html', {'noticias': noticias})
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