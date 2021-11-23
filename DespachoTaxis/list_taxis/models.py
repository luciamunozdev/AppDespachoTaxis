from django.db import models
from django.utils.html import format_html
# Create your models here.

class Taxi(models.Model): 
	Libre = 'Libre'
	Ocupado = 'Ocupado'
	estado_taxi_opciones = [
        (Libre, 'Libre'),
        (Ocupado, 'Ocupado'),
    ]
	estado_taxi = models.CharField(
        max_length=250,
        choices=estado_taxi_opciones,
        default=Libre,
    )
	conductor = models.CharField(max_length=250,blank=None, null = False, unique=True)
	matricula = models.CharField(max_length=250, blank=None, null = False,  unique=True)
	ubicacion_actual = models.CharField(max_length=250, blank=None, null = False)
	destino = models.CharField(max_length=250, blank=True, null = True)
	coord_ubicacion_actual = models.FloatField( blank=None, null = True)
	coord_destino = models.FloatField(blank=None, null = True)
	
	def __str__(self):
		return f"Concuctor {self.conductor}"
  