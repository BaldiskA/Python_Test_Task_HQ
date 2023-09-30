from django.contrib.auth import get_user_model
from django.db.models import Sum
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from education.models import LessonAccess, Product

User = get_user_model()


class CustomUserSerializer(UserCreateSerializer):
    """Сериализатор для вывода пользователей."""

    class Meta:
        """Мета-параметры сериализатора"""
        model = User
        fields = ('email',
                  'id',
                  'username',
                  'first_name',
                  'last_name')


class CustomCreateUserSerializer(CustomUserSerializer):
    """Сериализатор для создания пользователя."""

    class Meta:
        """Мета."""
        model = User
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class LessonAccessSerializer(serializers.ModelSerializer):
    """Сериализатор для первого запроса."""
    user = CustomUserSerializer()

    class Meta:
        model = LessonAccess
        fields = ['id',
                  'viewing_time_seconds',
                  'is_completed',
                  'user',
                  'lesson']


class LessonAccessWithLastViewSerializer(serializers.ModelSerializer):
    """Сериализатор для второго запроса."""
    last_viewed = serializers.DateTimeField(
        source='last_viewed_time',
        read_only=True
        )

    class Meta:
        model = LessonAccess
        fields = ['lesson',
                  'viewing_time_seconds',
                  'is_completed',
                  'last_viewed']


class ProductStatsSerializer(serializers.ModelSerializer):
    """Сериализатор для третьего запроса."""
    total_lessons_viewed = serializers.SerializerMethodField()
    total_time_watched = serializers.SerializerMethodField()
    total_users = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'total_lessons_viewed',
                  'total_time_watched', 'total_users', 'purchase_percentage']

    def get_total_lessons_viewed(self, obj):
        """Количество просмотренных уроков от всех учеников."""
        return LessonAccess.objects.filter(
            lesson__products=obj,
            is_completed=True).count()

    def get_total_time_watched(self, obj):
        """Сколько в сумме все ученики потратили
        времени на просмотр роликов."""
        total_time = LessonAccess.objects.filter(
            lesson__products=obj,
            is_completed=True).aggregate(
                Sum('viewing_time_seconds'))
        return total_time['viewing_time_seconds__sum'] or 0

    def get_total_users(self, obj):
        """Количество учеников занимающихся на продукте."""
        return User.objects.filter(
            lessonaccess__lesson__products=obj).distinct().count()

    def get_purchase_percentage(self, obj):
        """Процент приобретения продукта."""
        total_users = User.objects.count()
        product_users = User.objects.filter(
            lessonaccess__lesson__products=obj).distinct().count()
        return (product_users / total_users) * 100 if total_users > 0 else 0
