from django.forms import ModelForm

from core.models import Address
from customer.models import User, Customer
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['national_code']

class AddressFrom(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['province', 'city', 'detail']