from django.contrib.auth import get_user_model


User = get_user_model()


class TestViewsIntegration:
    def test_user(self, client, db):
        User.objects.create_user(
            email="test@example.com",
            password="secret",
            first_name="Jane",
            last_name="Doe",
        )
        response = client.get("/users/")
        assert response.status_code == 200
        assert response.data[0]["email"] == "test@example.com"
        assert response.data[0]["is_staff"] is False

    def test_super_user(self, client, db):
        User.objects.create_superuser(
            email="test@example.com",
            password="secret",
            first_name="Jane",
            last_name="Doe",
        )
        response = client.get("/users/")
        assert response.status_code == 200
        assert response.data[0]["is_staff"] is True
