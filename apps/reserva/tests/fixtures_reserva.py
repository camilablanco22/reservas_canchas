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


@pytest.fixture
def get_reservas(get_canchas, get_turno, get_user_generico):
    cancha1, cancha2 = get_canchas
    turno = get_turno
    fecha = "2025-05-29"

    reserva1, _ = Reserva.objects.get_or_create(
        fecha=fecha,
        turno=turno,
        cancha=cancha1,
        defaults={
            "usuario": get_user_generico,
        }
    )
    reserva2, _ = Reserva.objects.get_or_create(
        fecha=fecha,
        turno=turno,
        cancha=cancha2,
        defaults={
            "usuario": get_user_generico,
        }
    )
    return reserva1, reserva2