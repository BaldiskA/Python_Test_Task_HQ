from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser):
    """Модель пользователей."""

    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Введите почту',
        max_length=254,
        unique=True
    )
    username = models.CharField(
        verbose_name='Уникальный юзернейм',
        help_text='Введите юзернейм',
        max_length=150,
        unique=True,
        db_index=True,
        validators=(UnicodeUsernameValidator(),)
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        help_text='Введите имя',
        db_index=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        help_text='Введите фамилию',
        db_index=True
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150,
        help_text='Введите пароль',
    )

    class Meta:
        """Класс мета."""

        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

    def __str__(self):
        """Строковое представление модели."""
        return self.username
