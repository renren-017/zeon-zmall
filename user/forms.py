from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class SignupForm(UserCreationForm):
    username = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
