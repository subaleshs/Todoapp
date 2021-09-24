from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class registerForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email','username','password1','password2']

