import pytest
from pytest_django.fixtures import client
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta
from .fixtures_user import get_authenticated_client, get_user_generico, api_client,  get_intruso
from .fixtures_cancha import get_cancha, get_canchas
from .fixtures_turno import get_turno
from .fixtures_reserva import get_reservas, get_reserva

@pytest.mark.django_db
@pytest.mark.parametrize("fecha_invalida, expected_error", [
    (str(date.today()), "No se permiten reservas para el mismo día." ),  # No permite reservas para hoy
    (str(date.today() - timedelta(days=1)), "La fecha de la reserva no puede ser anterior a la fecha actual.")  # No permite fechas pasadas
])
def test_crear_reserva_fecha_invalida(get_authenticated_client, get_cancha, get_turno, fecha_invalida, expected_error):
    client = get_authenticated_client

    data = {
        "fecha": fecha_invalida,
        "cancha": get_cancha.id,
        "turno": get_turno.id
    }

    response = client.post("/api/reserva/", data=data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert expected_error.lower() in str(response.data["fecha"][0]).lower()



def test_crear_reserva_cancha_ocupada(get_authenticated_client, get_cancha, get_turno, get_reserva):
    client = get_authenticated_client
    cancha = get_cancha
    turno = get_turno
    reserva = get_reserva










