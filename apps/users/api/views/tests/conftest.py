import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ....models.email_user import EmailUser

TEST_PASSWORD = "secret123"  # pragma: allowlist secret


@pytest.fixture
def user_model() -> type[EmailUser]:
    return EmailUser


@pytest.fixture
def auth_client(user_model: type[EmailUser], db: None):
    api_client = APIClient()
    admin_user = user_model.objects.create_superuser(
        email="admin@example.com",
        password=TEST_PASSWORD,
        first_name="Admin",
        last_name="User",
    )
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client
