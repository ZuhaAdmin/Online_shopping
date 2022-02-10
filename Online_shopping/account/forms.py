from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Registerform(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username"}))
    email = forms.EmailField(widget = forms.TextInput(attrs={"placeholder":"email"}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"re-password"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class Loginform(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))

    class Meta:
        model = User
        fields = ("username", "password")