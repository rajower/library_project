# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email']  # Include any additional fields you want in the registration form

class CustomAuthenticationForm(AuthenticationForm):
    pass
