from rest_framework import viewsets

from .models import Category, Tag, Product, Order, OrderItem
from .serializers import CategorySerializer, TagSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(title__iexact="Food")
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.filter(product__cost__exact=12)
    serializer_class = OrderItemSerializer
