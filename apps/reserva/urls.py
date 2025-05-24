from django.urls import path
from rest_framework.urls import app_name

from apps.reserva.api import TurnosDisponiblesPorCanchaView
from apps.reserva.models import Reserva

app_name = 'reserva'
urlpatterns = [
    path('disponibilidad/', TurnosDisponiblesPorCanchaView.as_view()),
]