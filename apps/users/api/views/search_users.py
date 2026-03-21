from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from .serializers import UserSerializer

User = get_user_model()


class UserSearchView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        email = self.request.query_params.get("email")
        return get_object_or_404(User, email=email)
