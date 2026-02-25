from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import EmailUser


class EmailUserAdmin(UserAdmin):
    model = EmailUser
    list_display = ["email", "first_name", "last_name", "is_staff"]
    list_filter = ["is_staff", "is_active"]
    ordering = ("email", "-date_joined")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )

    search_fields = ["email", "first_name", "last_name"]


admin.site.register(EmailUser, EmailUserAdmin)
