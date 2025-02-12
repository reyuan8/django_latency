from rest_framework import authentication, exceptions

from authentication.models import Token


class ExpiringTokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return None

        token_key = auth_header.split(" ")[1]
        try:
            token = Token.objects.get(key=token_key)
        except:
            raise exceptions.AuthenticationFailed("Invalid token")

        if token.is_expired:
            raise exceptions.AuthenticationFailed("Token expired")

        if request.path not in ["/signin", "/signup"]:
            token.save()

        return (token.user, token)
