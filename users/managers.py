from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from users.utils import validate_phone


class CustomUserManager(UserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The username field must be set")

        try:
            validate_email(username)
            id_type = "email"
        except ValidationError:
            validate_phone(username)
            id_type = "phone"

        user = self.model(username=username, id_type=id_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
