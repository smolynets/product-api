import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


@pytest.fixture
def auth_client(client):
    test_user = User.objects.create_user(username='testuser', password='testpassword')
    access_token = get_token_for_user(test_user)
    client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
    return client
