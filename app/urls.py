from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm


urlpatterns = [
    path("", views.home, name="home-page"),
    path("about/", views.about, name="about-page"),
    path("contact/", views.contact, name="contact-page"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', views.address, name="address"),
    path("update-address/<int:pk>", views.UpdateAddress.as_view(), name="update-address"),

    #login authentication
    path('register/', views.CustomerRegistrationView.as_view(), name="customer-register"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/customerlogin.html', authentication_form=LoginForm), name="customer-login"),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/passwordreset.html', form_class=MyPasswordResetForm), name="password-reset"),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name="password-change"),
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name="password-change-done"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
