# Generated by Django 5.1.3 on 2024-12-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligaAPP', '0002_equipo_imagenequipo_jugador_imagenjugador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
