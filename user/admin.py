from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel

    list_display = ('first_name', 'last_name', "email",
                    'balance', 'bonus', "is_staff", "is_active",)
    list_filter = ('first_name', 'last_name', "email",
                   'balance', 'bonus', "is_staff", "is_active",)
    # fieldsets = (
    #     (None, {"fields": ("email", "password")}),
    #     ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         "classes": ("wide",),
    #         "fields": (
    #             "email", "password1", "password2", "is_staff",
    #             "is_active", "groups", "user_permissions"
    #         )}
    #     ),
    # )
    # search_fields = ("email",)
    ordering = ("id",)


admin.site.register(UserModel, CustomUserAdmin)
