from django.urls import path, include
from rest_framework import routers
from .views import RatingViewSet

router = routers.DefaultRouter()

router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/rate/', include('rest_framework.urls', namespace='rest_framework'))
]
