from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.TextInput()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ("username","email","password1","password2",)