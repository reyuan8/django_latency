from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.auth import ExpiringTokenAuthentication
from authentication.models import Token
from users.models import User
from users.serializers import AuthSerializer


class SignupView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data["id"]
            password = serializer.validated_data["password"]

            if User.objects.filter(username=username).exists():
                return Response(
                    {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
                )

            user = User.objects.create_user(
                username=username,
                password=password,
            )
            token = Token.objects.create(user=user)
            return Response(
                {"token": str(token.key), "id_type": user.id_type},
                status=status.HTTP_201_CREATED,
            )


class SigninView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data["id"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username, password=password)
            if user is None:
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
                )

            token = Token.objects.create(user=user)
            return Response({"token": str(token.key)})


class LogoutView(APIView):
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        remove_all = request.data.get("all", False)
        if remove_all:
            request.user.tokens.all().delete()
        else:
            if request.auth:
                request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
