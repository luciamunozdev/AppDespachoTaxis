from django.db import models

# Create your models here.

class viaje(models.Model):
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    fecha = models.DateField()
    hora = models.TimeField()
