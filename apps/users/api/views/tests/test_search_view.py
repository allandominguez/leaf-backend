import pytest

from .conftest import TEST_PASSWORD


@pytest.mark.integration
class TestUserSearchViewIntegration:
    def test_user(self, user_model, auth_client):
        email = "test@example.com"
        user_model.objects.create_user(
            email=email,
            password=TEST_PASSWORD,
            first_name="Jane",
            last_name="Doe",
        )
        response = auth_client.get(f"/users/search/email/?email={email}")
        assert response.status_code == 200
        assert response.data["first_name"] == "Jane"
        assert response.data["is_staff"] is False

    def test_superuser(self, user_model, auth_client):
        email = "test@example.com"
        user_model.objects.create_superuser(
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
