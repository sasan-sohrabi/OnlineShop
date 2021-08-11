from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from customer.models import User
from django import forms


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
