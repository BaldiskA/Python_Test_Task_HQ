from django.contrib import admin
from django.urls import include, path

from api.views import ProductLessonAccessListAPIView, ProductStatsListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api/product-lesson-access/<int:product_id>/',
         ProductLessonAccessListAPIView.as_view(),
         name='product-lesson-access-list'),
    path('api/product-stats/',
         ProductStatsListAPIView.as_view(),
         name='product-stats-list'),
]
