import pytest
from rest_framework import status
from .fixtures_user import get_authenticated_client, get_user_generico, api_client,  get_intruso

@pytest.mark.django_db
def test_api_crear_cancha(get_authenticated_client):
    client = get_authenticated_client

    data = {
        "numero": 5,
        "superficie": "SINTETICO",
        "precio_por_hora": 1800.00,
        "activa": True
    }

    response = client.post(f'/api/cancha/', data=data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["numero"] == 5
    assert response.data["superficie"] == "SINTETICO"
    assert float(response.data["precio_por_hora"]) == 1800.00
