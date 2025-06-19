import pytest
from pytest_django.fixtures import client
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta
from .fixtures_user import get_authenticated_client, get_user_generico, api_client, get_usuario_solo_view_reserva
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


@pytest.mark.django_db
def test_crear_reserva_cancha_ocupada(get_authenticated_client, get_cancha, get_turno, get_reserva):
    client = get_authenticated_client

    reserva_existente = get_reserva  # Ya ocupa la cancha + turno + fecha

    data = {
        'fecha': reserva_existente.fecha,  # Mismo día
        'turno': reserva_existente.turno.id,
        'cancha': reserva_existente.cancha.id
    }

    response = client.post(f"/api/reserva/", data=data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'La cancha ya está reservada para ese turno.' in str(response.data)

@pytest.mark.django_db
def test_get_reservas_sin_autenticar(api_client, get_reservas):

    cliente = api_client
    response = cliente.get(f'/api/reserva/')

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_get_reserva_ajena(get_usuario_solo_view_reserva, get_reserva):
    reserva = get_reserva
    client, user = get_usuario_solo_view_reserva
    response = client.get(f'/api/reserva/{reserva.uuid}/')

    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert 'No puedes acceder a esta reserva.' in str(response.data)











