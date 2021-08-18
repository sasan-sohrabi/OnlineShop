from rest_framework import serializers

from order.models import OrderedProduct, Ordered


class OrderedProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    orders = OrderedProductSerializers(many=True)

    class Meta:
        model = Ordered
        fields = "__all__"


class OrderedProductSerializers_1(serializers.ModelSerializer):
    order_id = OrderSerializer()

    class Meta:
        model = OrderedProduct
        fields = "__all__"
