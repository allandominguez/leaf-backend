from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request

from .serializers import UserSerializer

User = get_user_model()


class UserSearchView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()

    def get_object(self) -> User:
        request: Request = self.request  # type: ignore[assignment]
        email = request.query_params.get("email")
        if not email:
            raise ValidationError({"email": "This query parameter is required."})
        return get_object_or_404(self.get_queryset(), email=email)
