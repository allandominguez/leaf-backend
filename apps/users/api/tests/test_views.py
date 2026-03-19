import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def auth_client(db):
    api_client = APIClient()
    admin_user = User.objects.create_superuser(
        email="admin@example.com",
        password="secret",  # pragma: allowlist secret
        first_name="Admin",
        last_name="User",
    )
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client


class TestUserListViewIntegration:
    def test_admin_user(self, auth_client):
        response = auth_client.get("/users/")
        assert response.status_code == 200

    def test_user_details(self, db):
        api_client = APIClient()
        user = User.objects.create_superuser(
            email="admin@example.com",
            password="secret",  # pragma: allowlist secret
            first_name="Jane",
            last_name="Doe",
        )
        refresh = RefreshToken.for_user(user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        response = api_client.get("/users/")
        assert response.data[0]["first_name"] == "Jane"
        assert response.data[0]["last_name"] == "Doe"
        assert response.data[0]["is_staff"] is True


@pytest.mark.integration
class TestUserSearchViewIntegration:
    def test_user(self, auth_client):
        email = "test@example.com"
        User.objects.create_user(
            email=email,
            password="secret",  # pragma: allowlist secret
            first_name="Jane",
            last_name="Doe",
        )
        response = auth_client.get(f"/users/search/email/?email={email}")
        assert response.status_code == 200
        assert response.data["first_name"] == "Jane"
        assert response.data["is_staff"] is False

    def test_superuser(self, auth_client):
        email = "test@example.com"
        User.objects.create_superuser(
            email=email,
            password="secret",  # pragma: allowlist secret
            first_name="Jane",
            last_name="Doe",
        )
        response = auth_client.get(f"/users/search/email/?email={email}")
        assert response.status_code == 200
        assert response.data["first_name"] == "Jane"
        assert response.data["is_staff"] is True

    def test_non_existing_user(self, auth_client):
        response = auth_client.get("/users/search/email/?email=test@example.com")
        assert response.status_code == 404


@pytest.mark.integration
class TestUserCreateViewIntegration:
    def test_create_user_success(self, db):
        api_client = APIClient()
        payload = {
            "email": "newuser@example.com",
            "password": "securepass123",  # pragma: allowlist secret
            "first_name": "John",
            "last_name": "Doe",
        }
        response = api_client.post("/users/register/", payload)
        assert response.status_code == 201
        assert response.data["email"] == "newuser@example.com"
        assert "password" not in response.data  # write_only field
        assert User.objects.filter(email="newuser@example.com").exists()

    def test_failed_short_password(self, db):
        api_client = APIClient()
        payload = {
            "email": "newuser@example.com",
            "password": "1234567",  # pragma: allowlist secret
            "first_name": "John",
            "last_name": "Doe",
        }
        response = api_client.post("/users/register/", payload)
        assert response.status_code == 400
        assert "password" in response.data

    def test_failed_missing_fields(self, db):
        api_client = APIClient()
        payload = {
            "email": "newuser@example.com",
        }
        response = api_client.post("/users/register/", payload)
        assert response.status_code == 400
        assert "password" in response.data
        assert "first_name" in response.data
        assert "last_name" in response.data

    def test_failed_existing_user(self, db):
        User.objects.create_user(
            email="newuser@example.com",
            password="securepass123",  # pragma: allowlist secret
            first_name="John",
            last_name="Doe",
        )
        api_client = APIClient()
        payload = {
            "email": "newuser@example.com",
            "password": "securepass123",  # pragma: allowlist secret
            "first_name": "John",
            "last_name": "Doe",
        }
        response = api_client.post("/users/register/", payload)
        assert response.status_code == 400
        assert "email" in response.data
