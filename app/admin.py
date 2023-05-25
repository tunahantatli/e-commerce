from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Product, Customer, Cart, Payment, OrderPlaced, Wishlist


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
    def products(self,obj):
        link=reverse('admin:app_product_change',args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=[
        'id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id', 'paid'
    ]

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user', 'customer', 'product', 'quantity', 'order_date', 'status', 'payment']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=['id','user', 'product']
    def products(self,obj):
        link=reverse('admin:app_product_change',args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)