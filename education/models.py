"""Модели продукт, урок и просмотр."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    """Модель продукта."""
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название продукта',
    )
    owner = models.ForeignKey(User,
                              verbose_name='Владелец продукта',
                              on_delete=models.CASCADE,
                              )

    def __str__(self):
        """Строковое представление."""
        return f'{self.title}, {self.owner}'

    class Meta:
        """Класс мета."""

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    """Модель урока."""
    products = models.ManyToManyField(Product)
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название урока',
        )
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField(
        verbose_name='Длительность в секундах',
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class LessonAccess(models.Model):
    """Модель доступа к урокам."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE
        )
    viewing_time_seconds = models.PositiveIntegerField(
        default=0,
        verbose_name='Время просмотра в секундах'
        )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Просмотрено',
        )
    last_viewed_time = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата просмотра',
    )

    def __str__(self):
        """Строковое представление модели."""
        return f'{self.lesson} {self.user} {self.viewing_time_seconds}'

    class Meta:
        """Класс мета."""
        verbose_name = 'просмотры уроков'
        verbose_name_plural = 'просмотры уроков'