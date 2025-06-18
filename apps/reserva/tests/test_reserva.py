import pytest
from pytest_django.fixtures import client
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta
from .fixtures_user import get_authenticated_client, get_user_generico, api_client,  get_intruso
from .fixtures_cancha import get_cancha, get_canchas
from .fixtures_turno import get_turno
from .fixtures_reserva import get_reservas, get_reserva

#Verificar que las operaciones CRUD funcionan correctamente
#GET
@pytest.mark.django_db
def test_api_lista_reservas(get_authenticated_client, get_reservas):
    cliente = get_authenticated_client
    cancha = get_cancha
    turno = get_turno
    reserva1, reserva2 = get_reservas
    response = cliente.get(f'/api/reserva/')

    data = response.data["results"]

    assert response.status_code == 200
    assert int(data[0]['cancha']) == reserva1.cancha.id # 1
    assert int(data[1]['cancha']) == reserva2.cancha.id  # 2

#POST
@pytest.mark.django_db
def test_crear_reserva(get_authenticated_client, get_cancha, get_turno):
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

#PUT
@pytest.mark.django_db
def test_editar_reserva(get_authenticated_client, get_canchas, get_turno, get_reserva):
    client = get_authenticated_client
    reserva = get_reserva
    cancha1, cancha2 = get_canchas
    turno = get_turno

#cambio la fecha para un día después
    data = {
        "fecha": str(date.today() + timedelta(days=2)),
        "cancha": cancha2.id,
        "turno": turno.id
    }

    response = client.put(f"/api/reserva/{reserva.uuid}/", data=data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data["cancha"] == cancha2.id
    assert response.data["fecha"] == str(date.today() + timedelta(days=2))






