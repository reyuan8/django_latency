import re

from django.core.exceptions import ValidationError


def validate_phone(value: str) -> None:
    phone_regex = re.compile(r"^\+?1?\d{9,15}$")
    if not phone_regex.match(value):
        raise ValidationError("Invalid phone number format.")
