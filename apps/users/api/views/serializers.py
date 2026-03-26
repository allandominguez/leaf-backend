from typing import Any, cast

from django.contrib.auth import get_user_model
from rest_framework import serializers

from ...models.email_user import EmailUser

User = cast("type[EmailUser]", get_user_model())


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    first_name = serializers.CharField(max_length=30, allow_blank=False, required=True)
    last_name = serializers.CharField(max_length=30, allow_blank=False, required=True)

    class Meta:  # type: ignore[override]
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "date_joined",
        ]

    def validate_email(self, value: str) -> str:
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data: dict[str, Any]) -> Any:
        return User.objects.create_user(**validated_data)
