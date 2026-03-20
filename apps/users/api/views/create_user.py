from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, throttling

from .serializers import UserSerializer

User = get_user_model()


class SignupThrottle(throttling.AnonRateThrottle):
    scope = "signup"


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    throttle_classes = [SignupThrottle]
