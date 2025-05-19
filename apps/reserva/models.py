
from django.db import models

from apps.usuario.models import Usuario
from reservas_canchas import settings

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


class Turno(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"


class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, blank=True, null=True)
    activa = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = ('fecha', 'cancha', 'turno')  #no puede existir más de una reserva con la misma combinación de...



