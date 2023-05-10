from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'title',
        'category',
        'selling_price',
        'discount_price',
        'product_image'
    ]