from django.contrib import admin
from .models import Product, Customer, Cart

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

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'user',
        'locality',
        'state',
        'zipcode',
    ]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'product', 'quantity']