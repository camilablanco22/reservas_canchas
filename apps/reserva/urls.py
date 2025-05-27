from django.urls import path

from apps.reserva.api.api import TurnosDisponiblesPorCanchaView


app_name = 'reserva'
urlpatterns = [
    path('disponibilidad/', TurnosDisponiblesPorCanchaView.as_view()),
]