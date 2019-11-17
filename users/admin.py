from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models


class RoomInline(admin.TabularInline):
    model = room_models.Room


@admin.register(models.User)  # decorator
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profie",
            {
                "fields": (
                    "gender",
                    "avatar",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    inlines = [RoomInline]

