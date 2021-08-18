from rest_framework import serializers

from core.models import User, Address
from customer.models import Customer


class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone', 'first_name', 'last_name', 'email']


class UserSerializer(serializers.ModelSerializer):
    customers = CustomerSerializers(many=True)
    addresses = AddressSerializer(many=True)

    class Meta:
        model = User
        exclude = ['password']


class CustomerSerializers_1(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
