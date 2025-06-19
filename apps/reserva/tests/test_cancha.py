import pytest
from rest_framework import status
from .fixtures_user import get_authenticated_client, get_user_generico, api_client
from .fixtures_cancha import get_canchas

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

@pytest.mark.django_db
@pytest.mark.parametrize("campo, valor, error_esperado", [
    ("numero", "2", "cancha with this numero already exists."),
    ("precio_por_hora", "100000000000", "Ensure that there are no more than 10 digits in total.")
])
def test_api_crear_cancha_fallida(get_authenticated_client, get_canchas, campo, valor, error_esperado):
    client = get_authenticated_client

    data = {
        campo:valor,
        "superficie": "SINTETICO",
        "activa": True
    }

    response = client.post(f'/api/cancha/', data=data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert error_esperado.lower() in str(response.data[campo][0]).lower()