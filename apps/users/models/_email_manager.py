from typing import Any, Optional

from django.contrib.auth.models import BaseUserManager


class InvalidCredential(ValueError):
    """Raised when invalid user credential passed."""

    def __init__(self, message: str = "Invalid user credential"):
        self.message = message
        super().__init__(self.message)


class EmailUserManager(BaseUserManager):
    def create_user(
        self, email: str, password: Optional[str] = None, **extra_fields: Any
    ):
        if not email:
            raise InvalidCredential("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email: str, password: Optional[str] = None, **extra_fields: Any
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise InvalidCredential("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise InvalidCredential("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
