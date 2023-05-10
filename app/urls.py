from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("about/", views.about, name="about-page"),
    path("contact/", views.contact, name="contact-page"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category")
]