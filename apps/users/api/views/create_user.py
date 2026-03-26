from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from .serializers import UserSerializer

User = get_user_model()


class IsAnonymousUser(BasePermission):
    message = "Authenticated users may not register a new account."

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.user.is_anonymous


class SignupThrottle(AnonRateThrottle):
    scope = "signup"


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAnonymousUser]
    throttle_classes = [SignupThrottle]
