import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        email="admin@example.com",
        password="secret",  # pragma: allowlist secret
        first_name="Admin",
        last_name="User",
    )


class TestUserListViewIntegration:
    def test_admin_user(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get("/users/")
        assert response.status_code == 200

    def test_user_details(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get("/users/")
        assert response.status_code == 200
        assert response.data[0]["first_name"] == "Admin"
        assert response.data[0]["last_name"] == "User"
        assert response.data[0]["is_staff"] is True


@pytest.mark.integration
class TestUserSearchViewIntegration:
    def test_user(self, client, admin_user):
        User.objects.create_user(
            email="test@example.com",
            password="secret",  # pragma: allowlist secret
            first_name="Jane",
            last_name="Doe",
        )
        client.force_login(admin_user)
        response = client.get("/users/search/email/?email=test@example.com")
        assert response.status_code == 200
        assert response.data["first_name"] == "Jane"
        assert response.data["is_staff"] is False

    def test_superuser(self, client, admin_user):
        User.objects.create_superuser(
            email="test@example.com",
            password="secret",  # pragma: allowlist secret
            first_name="Jane",
            last_name="Doe",
        )
        client.force_login(admin_user)
        response = client.get("/users/search/email/?email=test@example.com")
        assert response.status_code == 200
        assert response.data["first_name"] == "Jane"
        assert response.data["is_staff"] is True

    def test_non_existing_user(self, client, admin_user):
        client.force_login(admin_user)
        response = client.get("/users/search/email/?email=test@example.com")
        assert response.status_code == 404
