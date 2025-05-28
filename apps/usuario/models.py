from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    dni = models.PositiveIntegerField(unique=True, blank=True, null=True)
    telefono = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username}'

    def obtener_nombre_completo(self):
        if self.last_name and self.first_name:
            return f'{self.last_name}, {self.first_name}'.strip()
        return self.username

    obtener_nombre_completo.short_description = 'Nombre Completo'