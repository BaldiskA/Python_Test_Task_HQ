from django.urls import include, path
from rest_framework import routers

from .views import CustomUserViewSet, LessonAccessViewSet

router = routers.DefaultRouter()

router.register('taskone', LessonAccessViewSet, basename='taskone')
router.register('users', CustomUserViewSet, basename='users')
app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
