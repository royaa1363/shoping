from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, TagViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)
router.register('product', ProductViewSet)
router.register('order', OrderViewSet)
router.register('orderitem', OrderItemViewSet)


urlpatterns = [
    path('', include(router.urls))
]
