from decimal import Decimal

import pytest
from pytest_django.fixtures import client
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta, datetime

from reservas_canchas import settings_testing
from .fixtures_user import get_authenticated_client, get_user_generico, api_client
from .fixtures_cancha import get_cancha, get_canchas
from .fixtures_turno import get_turno
from .fixtures_reserva import get_reservas, get_reserva
from ..api.conversion import calcular_duracion_en_horas
import requests


#Verificar que las operaciones CRUD funcionan correctamente
#GET
@pytest.mark.django_db
def test_api_lista_reservas(get_authenticated_client, get_reservas):
    cliente = get_authenticated_client
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

    # Calcula el total esperado
    total_esperado = cancha.precio_por_hora * calcular_duracion_en_horas(turno) #Calculo el precio de otra forma para asegurar que es el correcto
    assert Decimal(response.data["total"]) == total_esperado

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

#SIMULACIÓN CONSUMO DE API
@pytest.mark.django_db
def test_api_consumo_api(get_authenticated_client, get_reserva):
    cliente = get_authenticated_client
    reserva = get_reserva

    #obtención tasa de cambio
    url = f"https://v6.exchangerate-api.com/v6/{settings_testing.EXCHANGE_API_KEY}/latest/ARS"
    response_usd = requests.get(url)
    response_usd.raise_for_status()
    data_usd = response_usd.json()
    tasa = data_usd['conversion_rates'].get('USD')

    monto_USD = round(reserva.total * Decimal(str(tasa)), 2)

    response = cliente.get(f'/api/reserva/')
    data = response.data["results"]

    assert data[0]['total_usd'] == monto_USD




