"""
JWT token handling managed by Simple JWT's `TokenObtainPairView` and `TokenRefreshView`.
These tests will verify our user creation with JWT's interface.
"""

from datetime import timedelta

import pytest
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .conftest import TEST_PASSWORD


@pytest.mark.integration
class TestTokenObtainPairView:
    def test_valid_credentials(self, user_model, db):
        api_client = APIClient()
        email = "test@example.com"
        user_model.objects.create_user(
            email=email,
            password=TEST_PASSWORD,
            first_name="Jane",
            last_name="Doe",
        )
        payload = {"email": email, "password": TEST_PASSWORD}
        response = api_client.post("/api/token/", payload)
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data

    def test_invalid_password(self, user_model, db):
        api_client = APIClient()
        email = "test@example.com"
        user_model.objects.create_user(
            email=email,
            password=TEST_PASSWORD,
            first_name="Jane",
            last_name="Doe",
        )
        payload = {"email": email, "password": "invalid"}  # pragma: allowlist secret
        response = api_client.post("/api/token/", payload)
        assert response.status_code == 401

    def test_nonexistent_user(self, db):
        api_client = APIClient()
        payload = {
            "email": "test@example.com",
            "password": TEST_PASSWORD,
        }
        response = api_client.post("/api/token/", payload)
        assert response.status_code == 401


@pytest.mark.integration
class TestTokenRefreshView:
    @pytest.fixture
    def user(self, user_model, db):
        return user_model.objects.create_user(
            email="test@example.com",
            password=TEST_PASSWORD,
            first_name="Jane",
            last_name="Doe",
        )

    def test_valid_token(self, user):
        api_client = APIClient()
        refresh = RefreshToken.for_user(user)
        response = api_client.post("/api/token/refresh/", {"refresh": refresh})
        assert response.status_code == 200
        assert "access" in response.data

    def test_invalid_token(self):
        api_client = APIClient()
        payload = {"refresh": "invalid"}
        response = api_client.post("/api/token/refresh/", payload)
        assert response.status_code == 401

    def test_expired_token(self, user):
        refresh = RefreshToken.for_user(user)
        # Backdate the expiry to make the token already expired
        refresh.payload["exp"] = (timezone.now() - timedelta(seconds=1)).timestamp()
        api_client = APIClient()
        response = api_client.post("/api/token/refresh/", {"refresh": refresh})
        assert response.status_code == 401
