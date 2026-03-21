from unittest.mock import Mock

import pytest
from django.contrib.auth import get_user_model

from ..serializers import UserSerializer
from .conftest import TEST_PASSWORD

User = get_user_model()


class TestUserSerializersUnit:
    def test_data(self):
        user = Mock(
            id=1,
            email="test@example.com",
            first_name="Jane",
            last_name="Doe",
            is_active=True,
            is_staff=False,
            date_joined="20260101",
        )
        serializer = UserSerializer(user)
        assert serializer.data == {
            "id": 1,
            "email": "test@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "is_active": True,
            "is_staff": False,
            "date_joined": "20260101",
        }


@pytest.mark.integration
class TestUserSerializersIntegration:
    def test_user_data(self, db):
        user = User.objects.create_user(
            email="test@example.com",
            password=TEST_PASSWORD,
            first_name="Jane",
            last_name="Doe",
        )
        serializer = UserSerializer(user)
        assert serializer.data["email"] == "test@example.com"
        assert serializer.data["first_name"] == "Jane"
        assert serializer.data["last_name"] == "Doe"
        assert serializer.data["is_active"] is True
        assert serializer.data["is_staff"] is False
        assert serializer.data["date_joined"] == user.date_joined.isoformat().replace(
            "+00:00", "Z"
        )

    def test_superuser_data(self, db):
        user = User.objects.create_superuser(
            email="test2@example.com",
            password=TEST_PASSWORD,
            first_name="John",
            last_name="Smith",
        )
        serializer = UserSerializer(user)
        assert serializer.data["email"] == "test2@example.com"
        assert serializer.data["first_name"] == "John"
        assert serializer.data["last_name"] == "Smith"
        assert serializer.data["is_active"] is True
        assert serializer.data["is_staff"] is True
        assert serializer.data["date_joined"] == user.date_joined.isoformat().replace(
            "+00:00", "Z"
        )
