from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


User = get_user_model()


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
