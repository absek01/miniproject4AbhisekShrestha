# forms.py

from django import forms
from .models import ExampleModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ['title', 'description']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
