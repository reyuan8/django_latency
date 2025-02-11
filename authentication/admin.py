from django.contrib import admin

from authentication.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    fields = ("user", "key", "updated")
    readonly_fields = ("user", "key", "updated")
