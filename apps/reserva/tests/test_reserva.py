import pytest
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta
from .fixtures_user import get_authenticated_client, get_user_generico, api_client,  get_intruso
from .fixtures_cancha import get_cancha
from .fixtures_turno import get_turno


@pytest.mark.django_db
def test_api_crear_reserva(get_authenticated_client, get_cancha, get_turno):
    client = get_authenticated_client
    cancha = get_cancha
    turno = get_turno

    data = {
        "fecha": str(date.today() + timedelta(days=1)), #FECHA DE MAÑANA, YA QUE NO PERMITE RESERVAS PARA HOY
        "cancha": cancha.id,
        "turno": turno.id
    }

    response = client.post(f'/api/reserva/', data=data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["cancha"] == get_cancha.id
    assert response.data["turno"] == get_turno.id
