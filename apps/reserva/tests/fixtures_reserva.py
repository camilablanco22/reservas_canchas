import pytest
from .fixtures_user import get_authenticated_client, get_user_generico, api_client
from apps.reserva.models import Reserva


@pytest.fixture
def get_reserva(get_cancha, get_turno, get_user_generico):
    cancha = get_cancha
    turno = get_turno
    fecha = "2025-05-29"

    reserva, _ = Reserva.objects.get_or_create(
        fecha=fecha,
        turno=turno,
        cancha=cancha,
        defaults={
            "usuario": get_user_generico,
        }
    )
    return reserva
