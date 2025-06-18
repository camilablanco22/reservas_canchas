import pytest
from pytest_django.fixtures import client
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta
from .fixtures_user import get_authenticated_client, get_user_generico, api_client,  get_intruso
from .fixtures_cancha import get_cancha, get_canchas
from .fixtures_turno import get_turno
from ..models import Turno


#verificar la única validacion que aplica para turno

@pytest.mark.django_db
def test_crear_turno(get_authenticated_client):
    client = get_authenticated_client

    data = {
        "hora_inicio": "19:00:00",
        "hora_fin": "20:00:00"

    }

    response = client.post(f'/api/turno/', data=data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Turno.objects.filter(hora_inicio='19:00:00',hora_fin="20:00:00").count() == 1
    assert response.data["hora_inicio"] == "19:00:00"
    assert response.data["hora_fin"] == "20:00:00"

@pytest.mark.django_db
def test_crear_turno_fallido(get_authenticated_client):
    client = get_authenticated_client

    data = {
        "hora_inicio": "21:00:00",
        "hora_fin": "20:00:00"
    }

    response = client.post(f'/api/turno/', data=data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "la hora de inicio no puede ser posterior a la hora de fin" in str(response.data["non_field_errors"][0]).lower()