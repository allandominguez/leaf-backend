import pytest

from ..models import EmailUser


class TestEmailUser:
    def test_email_user_str(self):
        email = "test@example.com"
        user = EmailUser(email=email)
        assert str(user) == email

    def test_email_user_creation(self):
        email = "user@example.com"
        first_name = "John"
        last_name = "Doe"
        user = EmailUser(email=email, first_name=first_name, last_name=last_name)
        assert user.email == email
        assert user.first_name == first_name
        assert user.last_name == last_name
        assert user.is_active is True
        assert user.is_staff is False

    def test_email_user_defaults(self):
        user = EmailUser(email="test@example.com")
        assert user.is_active is True
        assert user.is_staff is False


@pytest.mark.integration
class TestEmailUserIntegration:
    def test_email_user_saved_to_database(self, db):
        email = "integration@example.com"
        EmailUser.objects.create_user(
            email=email,
            password="testpass123",  # pragma: allowlist secret
        )
        retrieved_user = EmailUser.objects.get(email=email)
        assert retrieved_user.email == email
        assert str(retrieved_user) == email

    def test_email_user_uniqueness(self, db):
        email = "unique@example.com"
        EmailUser.objects.create_user(
            email=email,
            password="testpass123",  # pragma: allowlist secret
        )
        with pytest.raises(Exception):
            EmailUser.objects.create_user(
                email=email,
                password="testpass123",  # pragma: allowlist secret
            )

    def test_email_user_authentication(self, db):
        email = "auth@example.com"
        password = "testpass123"  # pragma: allowlist secret
        user = EmailUser.objects.create_user(email=email, password=password)
        assert user.check_password(password)
