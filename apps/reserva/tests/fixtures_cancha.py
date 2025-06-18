import pytest
from apps.reserva.models import Cancha
from decimal import Decimal

@pytest.fixture
def get_cancha():
    cancha, _ = Cancha.objects.get_or_create(
        numero=1,
        defaults={
            "superficie": "CEMENTO",
            "precio_por_hora": Decimal("15000.00"),
            "activa": True
        }
    )
    return cancha


@pytest.fixture
def get_canchas():
    cancha1, _ = Cancha.objects.get_or_create(
        numero=1,
        defaults={
            "superficie": "CEMENTO",
            "precio_por_hora": Decimal("15000.00"),
            "activa": True
        }
    )
    cancha2, _ = Cancha.objects.get_or_create(
        numero=2,
        defaults={
            "superficie": "CEMENTO",
            "precio_por_hora": Decimal("15000.00"),
            "activa": True
        }
    )

    return cancha1, cancha2