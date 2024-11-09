from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name='index'),

    path('listadoDeLigas/', views.listaLigas, name='listaLigas'),
    path('listadoDeEquipos/', views.listaEquipos, name='listaEquipos'),
    path('listadoDeJugadores/', views.listaJugadores, name='listaJugadores'),

    path('liga/<int:id_liga>/', views.detalleLiga, name='detalleLiga'),
    path('equipo/<int:id_equipo>/', views.detalleEquipo, name='detalleEquipo'),
    path('jugador/<int:id_jugador>/', views.detalleJugador, name='detalleJugador'),
]