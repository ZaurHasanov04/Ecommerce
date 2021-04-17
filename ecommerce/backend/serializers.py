from rest_framework import serializers
from billing.models import BillingProfile
from order.models import Order
from backend.models import User
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    cart=CartSerializer()
    class Meta:
        model = Order
        exclude=["billing_address", "shipping_address","billing_profile"]


class BillingSerializer(serializers.ModelSerializer):
    billing_profile=OrderSerializer(many=True, read_only=True)
    class Meta:
        model = BillingProfile
        exclude= ["user",]



class UserSerializer(serializers.ModelSerializer):
    billing_user=BillingSerializer()
    class Meta:
        model = User
        fields = ["billing_user",]