from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, throttling

from .serializers import UserSerializer

User = get_user_model()


class IsAnonymousUser(permissions.BasePermission):
    message = "Authenticated users may not register a new account."

    def has_permission(self, request, view):
        return request.user.is_anonymous


class SignupThrottle(throttling.AnonRateThrottle):
    scope = "signup"


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAnonymousUser]
    throttle_classes = [SignupThrottle]
