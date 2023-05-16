from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'True'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'True'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'True'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'username', 'password1', 'password2', 'email']

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'True'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}))
    
class MyPasswordResetForm(PasswordChangeForm):
    pass 