from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    # Define choices for the user type dropdown
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('staff', 'Staff'),
        ('superuser', 'Superuser'),
    )

    # Add a field for user type using ChoiceField
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        
        # Set the initial value of the user type based on the user's current status
        if self.instance.is_superuser:
            self.initial['user_type'] = 'superuser'
        elif self.instance.is_staff:
            self.initial['user_type'] = 'staff'
        else:
            self.initial['user_type'] = 'user'

