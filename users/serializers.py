from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="username")

    class Meta:
        model = User
        fields = ("id", "id_type")


class AuthSerializer(serializers.Serializer):
    id = serializers.CharField()
    password = serializers.CharField(write_only=True)
