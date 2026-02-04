from ..models import EmailUser


class TestEmailUser:
    def test_email_user_str(self):
        email = "test@example.com"
        user = EmailUser(email=email)
        assert str(user) == email
