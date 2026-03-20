import pytest
from django.core.cache import cache
from rest_framework.test import APIClient


@pytest.mark.integration
class TestUserCreateViewIntegration:
    @pytest.fixture(autouse=True)
    def clear_cache(self):
        cache.clear()
        yield
        cache.clear()

    def test_create_user_success(self, user_model, db):
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
        assert user_model.objects.filter(email="newuser@example.com").exists()

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

    def test_failed_existing_user(self, user_model, db):
        user_model.objects.create_user(
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

    def test_signup_rate_limit(self, db):
        client = APIClient()
        for i in range(5):
            payload = {
                "email": f"user{i}@example.com",
                "password": "securepass123",  # pragma: allowlist secret
                "first_name": "Jane",
                "last_name": "Doe",
            }
            resp = client.post("/users/register/", payload)
            assert resp.status_code == 201

        payload = {
            "email": "user5@example.com",
            "password": "securepass123",  # pragma: allowlist secret
            "first_name": "Jane",
            "last_name": "Doe",
        }
        resp = client.post("/users/register/", payload)
        assert resp.status_code == 429
        assert "throttled" in resp.data.get("detail", "").lower()
