from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class TestUserListViewIntegration:
    def test_admin_user(self, auth_client):
        response = auth_client.get("/users/")
        assert response.status_code == 200

    def test_user_details(self, user_model, db):
        api_client = APIClient()
        user = user_model.objects.create_superuser(
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
