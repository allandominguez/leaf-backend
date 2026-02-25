from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .serializers import UserSerializer

User = get_user_model()


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserSearchView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        email = self.request.query_params.get("email")
        return get_object_or_404(User, email=email)
