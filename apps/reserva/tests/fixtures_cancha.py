import pytest
from apps.reserva.models import Cancha

@pytest.fixture
def get_cancha():
    cancha, _ = Cancha.objects.get_or_create(
        numero=1,
        defaults={
            "superficie": "CEMENTO",
            "precio_por_hora": 15000.00,
            "activa": True
        }
    )
    return cancha
