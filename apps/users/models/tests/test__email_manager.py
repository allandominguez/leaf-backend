import pytest

from .._email_manager import EmailUserManager, InvalidCredential


class _DummyUser:
    def __init__(self, email=None, **extra_fields):
        self.email = email
        for k, v in extra_fields.items():
            setattr(self, k, v)

    def set_password(self, password):
        self.password = password

    def save(self, using=None):
        self.saved = True


class TestEmailUserManager:
    def test_no_email_raises_error(self):
        manager = EmailUserManager()
        with pytest.raises(InvalidCredential):
            manager.create_user(email=None)

    def test_email_is_normalized(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        user = manager.create_user(email="TeSt@ExAmPlE.COM")
        assert user.email == "TeSt@example.com"

    def test_password_saved(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        password = "Test Password123!"  # pragma: allowlist secret
        user = manager.create_user(email="test@example.com", password=password)
        assert user.password == password

    def test_user_saved(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        user = manager.create_user(email="test@example.com")
        assert user.saved is True

    def test_is_staff_true_for_superuser_when_missing(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        superuser = manager.create_superuser(email="test@example.com")
        assert superuser.is_staff is True

    def test_is_superuser_true_for_superuser_when_missing(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        superuser = manager.create_superuser(email="test@example.com")
        assert superuser.is_superuser is True

    def test_not_staff_raises_error(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        with pytest.raises(InvalidCredential):
            manager.create_superuser(email="test@example.com", is_staff=False)

    def test_not_superuser_raises_error(self):
        manager = EmailUserManager()
        manager.model = _DummyUser
        with pytest.raises(InvalidCredential):
            manager.create_superuser(email="test@example.com", is_superuser=False)
