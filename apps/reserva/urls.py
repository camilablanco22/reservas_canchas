from django.urls import path

from apps.reserva.api.api import TurnosDisponiblesPorCanchaView, TurnosDisponiblesPorFechaYCanchaView

app_name = 'reserva'
urlpatterns = [
    path('disponibilidad/', TurnosDisponiblesPorCanchaView.as_view()),
    path('disponibilidad/cancha/', TurnosDisponiblesPorFechaYCanchaView.as_view()),
]