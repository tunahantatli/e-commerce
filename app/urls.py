from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home-page"),
    path("about/", views.about, name="about-page"),
    path("contact/", views.contact, name="contact-page"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),

    #login authentication
    path('register/', views.CustomerRegistrationView.as_view(), name="customer-register"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
