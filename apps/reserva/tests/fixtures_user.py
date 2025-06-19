import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Permission

User = get_user_model()

def create_user(username, documento_identidad, first_name='Micaela', last_name='Salgado', password='unpassword', email=None, *, is_active=True, is_superuser=False, is_staff=False):
    email = '{}@root.com'.format(username) if email is None else email
    user, created = User.objects.get_or_create(username=username, email=email)

    if created:
        user.documento_identidad = documento_identidad
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.set_password(password)
        user.save()
    return user

def get_jwt_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def get_user_generico():
    return create_user(username='test_user', documento_identidad='44635875', first_name='Test', last_name='User', email='test@user.com', is_superuser=True, is_staff=True)

@pytest.fixture
def get_authenticated_client(get_user_generico, api_client):
    access_token = get_jwt_token_for_user(get_user_generico)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
    return api_client

@pytest.fixture
def get_usuario_sin_permisios(api_client):
    intruso = create_user(username="intruso", documento_identidad="99999999", first_name='intruso', last_name='intruso', email="intruso@root.com")
    access_token = get_jwt_token_for_user(intruso)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
    return api_client, intruso

@pytest.fixture
def get_usuario_solo_view_reserva(api_client):
    user = create_user(username="intruso", documento_identidad="99999999", first_name='intruso', last_name='intruso', email="intruso@root.com")

    # Asignar solo el permiso "view_reserva"
    permiso_view = Permission.objects.get(codename="view_reserva")
    user.user_permissions.set([permiso_view])

    access_token = get_jwt_token_for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
    return api_client, user