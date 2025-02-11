import uuid
from datetime import datetime, timedelta

from django.db import models

from users.models import User


class Token(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def is_expired(self):
        return datetime.now(self.updated.tzinfo) - self.updated > timedelta(minutes=5)

    def __str__(self):
        return (
            f"User={self.user.username}, key={self.key}, is_expired={self.is_expired}"
        )
