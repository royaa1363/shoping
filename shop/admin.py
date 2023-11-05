from django.contrib import admin
from star_rating.models import Rating
from .models import Category, Tag, Product, Order, OrderItem

admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Product)
# admin.site.register(Order)
admin.site.register(OrderItem)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'stock']
    search_fields = ['name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'product', 'score']


# admin.site.register(Rating, RatingAdmin)
