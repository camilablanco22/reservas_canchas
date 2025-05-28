from django.urls import path

from apps.reserva.api.api import TurnosDisponiblesPorFechaView, TurnosDisponiblesPorFechaYCanchaView

app_name = 'reserva'
urlpatterns = [
    path('disponibilidad/', TurnosDisponiblesPorFechaView.as_view()),
    path('disponibilidad/cancha/', TurnosDisponiblesPorFechaYCanchaView.as_view()),
]