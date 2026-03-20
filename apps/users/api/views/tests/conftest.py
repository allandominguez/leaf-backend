import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.fixture
def auth_client(user_model, db):
    api_client = APIClient()
    admin_user = user_model.objects.create_superuser(
        email="admin@example.com",
        password="secret",  # pragma: allowlist secret
        first_name="Admin",
        last_name="User",
    )
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client
