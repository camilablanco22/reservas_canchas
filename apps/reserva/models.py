
from django.db import models

from apps.usuario.models import Usuario


# Create your models here.

class Cancha(models.Model):
    SUPERFICIE_CHOICES = [
        ('CEMENTO', 'CEMENTO'),
        ('SINTETICO', 'SINTETICO')
    ]
    numero= models.PositiveIntegerField(unique=True)
    superficie= models.CharField(choices=SUPERFICIE_CHOICES)
    precio_por_hora = models.DecimalField(decimal_places=2, max_digits=10)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return str(self.numero)


class Reserva(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activa = models.BooleanField(default = True)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas' )
    precio_total = models.DecimalField(max_digits=10, decimal_places = 2, blank=True, null = True)
