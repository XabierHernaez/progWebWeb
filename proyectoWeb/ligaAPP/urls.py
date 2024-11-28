#from django.urls import path
#from . import views

# urlpatterns = [
#     path('inicio/', views.index, name='index'),

#     path('listadoDeLigas/', views.listaLigas, name='listaLigas'),
#     path('listadoDeEquipos/', views.listaEquipos, name='listaEquipos'),
#     path('listadoDeJugadores/', views.listaJugadores, name='listaJugadores'),

#     path('liga/<int:id_liga>/', views.detalleLiga, name='detalleLiga'),
#     path('equipo/<int:id_equipo>/', views.detalleEquipo, name='detalleEquipo'),
#     path('jugador/<int:id_jugador>/', views.detalleJugador, name='detalleJugador'),
# ]

from django.urls import path
from .views import (IndexView, listaLigas, listaEquipos, listaJugadores, 
                    DetalleLigaView, DetalleEquipoView, DetalleJugadorView)

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='index'),

    path('listadoDeLigas/', listaLigas.as_view(), name='listaLigas'),
    path('listadoDeEquipos/', listaEquipos.as_view(), name='listaEquipos'),
    path('listadoDeJugadores/', listaJugadores.as_view(), name='listaJugadores'),

    path('liga/<int:pk>/', DetalleLigaView.as_view(), name='detalleLiga'),
    path('equipo/<int:pk>/', DetalleEquipoView.as_view(), name='detalleEquipo'),
    path('jugador/<int:pk>/', DetalleJugadorView.as_view(), name='detalleJugador'),
]