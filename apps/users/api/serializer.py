from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    Currently a READ-only serializer on EmailUser.
    Should add field constraints when implementing create and update.
    """

    id = serializers.IntegerField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    date_joined = serializers.DateTimeField()
