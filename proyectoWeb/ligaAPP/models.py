from django.db import models

# Create your models here.

class Liga(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    anio = models.DateField()
    maximoGoleadorLiga = models.CharField(max_length=25)
    maximoAsistenteLiga = models.CharField(max_length=50)
    presidenteLiga = models.CharField(max_length=50)
    imagenLiga = models.URLField(max_length=600, null= True, blank=True)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    maximoGoleadorEquipo = models.CharField(max_length=50)
    maximoAsistenteEquipo = models.CharField(max_length=50)
    AnioCreacion = models.DateField()
    liga = models.ForeignKey(Liga, related_name = 'equipos', on_delete=models.CASCADE)
    imagenEquipo = models.URLField(max_length=600, null= True, blank=True)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    goles = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50, null= True, blank=True)
    anioDeUnion = models.DateField()
    fechaNacimiento = models.DateField()
    equipo = models.ForeignKey(Equipo, related_name = 'jugadores', on_delete=models.CASCADE)
    imagenJugador = models.URLField(max_length=600, null= True, blank=True)

    def __str__(self):
        return self.nombre +" "+ self.apellidos
