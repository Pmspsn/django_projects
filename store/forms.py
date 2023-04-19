from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-2", "placehoder":"Enter username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-2", "placehoder":"Enter email"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-2", "placehoder":"Enter password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-2", "placehoder":"Confirm password"}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    