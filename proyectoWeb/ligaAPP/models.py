from django.db import models

# Create your models here.

class Liga(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    anio = models.DateField()
    maximoGoleadorLiga = models.CharField(max_length=25)
    maximoAsistenteLiga = models.CharField(max_length=50)
    presidenteLiga = models.CharField(max_length=50)

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    maximoGoleadorEquipo = models.CharField(max_length=50)
    maximoAsistenteEquipo = models.CharField(max_length=50)
    AnioCreacion = models.DateField()
    liga = models.ForeignKey(Liga, related_name = 'equipos', on_delete=models.CASCADE)

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    goles = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    anioDeUnion = models.DateField()
    fechaNacimiento = models.DateField()
    equipo = models.ForeignKey(Equipo, related_name = 'jugadores', on_delete=models.CASCADE)
