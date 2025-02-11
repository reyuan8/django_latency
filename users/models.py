from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class User(AbstractUser):
    id_type = models.CharField(
        max_length=5, choices=[("email", "Email"), ("phone", "Phone")]
    )

    objects = CustomUserManager()

    def __str__(self):
        return f"Username={self.username}, id_type={self.id_type}"
