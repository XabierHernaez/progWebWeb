
from django.urls import path
from .views import (IndexView, listaLigas, listaEquipos, listaJugadores, 
                    DetalleLigaView, DetalleEquipoView, DetalleJugadorView, obtener_datos)

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='index'),

    path('listadoDeLigas/', listaLigas.as_view(), name='listaLigas'),
    path('listadoDeEquipos/', listaEquipos.as_view(), name='listaEquipos'),
    path('listadoDeJugadores/', listaJugadores.as_view(), name='listaJugadores'),

    path('liga/<int:pk>/', DetalleLigaView.as_view(), name='detalleLiga'),
    path('equipo/<int:pk>/', DetalleEquipoView.as_view(), name='detalleEquipo'),
    path('jugador/<int:pk>/', DetalleJugadorView.as_view(), name='detalleJugador'),

    path('obtener-datos/', obtener_datos, name='obtener_datos'),  # Aquí está la nueva ruta
]