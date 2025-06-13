import pytest
from datetime import time
from apps.reserva.models import Turno

@pytest.fixture
def get_turno():
    turno, _ = Turno.objects.get_or_create(
        hora_inicio=time(15, 0),
        hora_fin=time(16, 0)
    )
    return turno
