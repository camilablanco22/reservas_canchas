from datetime import datetime, date
from decimal import Decimal
from uuid import uuid4

from django.db import models

from apps.usuario.models import Usuario
from reservas_canchas import settings

class Cancha(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
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
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio.strftime('%H:%M')} - {self.hora_fin.strftime('%H:%M')}"


class Reserva(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, blank=True, null=True)
    activa = models.BooleanField(default=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def calcular_total(self):
        inicio = datetime.combine(date.min, self.turno.hora_inicio)
        fin = datetime.combine(date.min, self.turno.hora_fin)
        duracion_horas = Decimal((fin - inicio).seconds) / Decimal(3600)
        return self.cancha.precio_por_hora * duracion_horas

    def save(self, *args, **kwargs):
        self.total = self.calcular_total()
        super().save(*args, **kwargs)







