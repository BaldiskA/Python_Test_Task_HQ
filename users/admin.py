from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """Модель пользователя для админки."""

    list_display = ('pk', 'username', 'email', 'first_name', 'last_name',
                    'password')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')