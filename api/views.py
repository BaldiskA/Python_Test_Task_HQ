from djoser.views import UserViewSet
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import AllowAny

from education.models import LessonAccess, Product
from users.models import User

from .serializers import (CustomUserSerializer, LessonAccessSerializer,
                          LessonAccessWithLastViewSerializer,
                          ProductStatsSerializer)


class CustomUserViewSet(UserViewSet):
    """Вьюсет пользователей."""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)


class LessonAccessViewSet(viewsets.ReadOnlyModelViewSet):
    """Выведение списка всех уроков по всем продуктам
      к которым пользователь имеет доступ,
      с выведением информации о статусе и времени просмотра."""
    serializer_class = LessonAccessSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_accesses = LessonAccess.objects.filter(user=user)
        return user_accesses


class ProductLessonAccessListAPIView(generics.ListAPIView):
    """Выведение списка уроков по конкретному продукту
    к которому пользователь имеет доступ,
    с выведением информации о статусе и времени просмотра,
    а также датой последнего просмотра ролика."""
    serializer_class = LessonAccessWithLastViewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        user_accesses = LessonAccess.objects.filter(
            user=user, lesson__products__id=product_id
            )
        return user_accesses


class ProductStatsListAPIView(generics.ListAPIView):
    """Отображение статистики по продуктам. """
    queryset = Product.objects.all()
    serializer_class = ProductStatsSerializer
    permission_classes = [permissions.IsAuthenticated]
