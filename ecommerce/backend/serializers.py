from rest_framework import serializers
from billing.models import BillingProfile
from order.models import Order
from backend.models import User
from cart.models import Cart, CartProduct
from product.models import Product
from django.http import JsonResponse
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class TokenPairSerializers(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token=super(TokenPairSerializers,cls).save(user)

#         token['username']=user.username

#         return token



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"



class CartProductSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    # produkt=CartProductList(source="*")
    class Meta:
        model = CartProduct
        fields = "__all__"




class CartSerializer(serializers.ModelSerializer):
    products=CartProductSerializer(many=True)
    # produkt=CartProductList(source="*")
    class Meta:
        model = Cart
        fields="__all__"



class OrderSerializer(serializers.ModelSerializer):
    carting=serializers.SerializerMethodField(source="*")
    class Meta:
        model = Order
        exclude=["billing_address", "shipping_address","billing_profile","id",]
    def get_carting(self, obj):
        data=obj.cart.products.all()
        for x in data:
            print(x.product)
            bomb=Product.objects.filter(product_name=x.product).values("product_name","product_price","product_discount","product_discount_price")
        for a in bomb:
            name=obj.billing_profile.user.username
            datas={
                "profile":obj.billing_profile.user.username,
                "product detail":a,
            }
            return datas



# class CartListSerializers(serializers.Field):
#     def to_representation(self, value):
#         data=value.cart.products.all()
#         for x in data:
#             print(x.product)
#             bomb=Product.objects.all().filter(product_name=x.product).values()
#         for a in bomb:
#             return a
        



# class BillingSerializer(serializers.ModelSerializer):
#     billing_profile=OrderSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = BillingProfile
#         fields="__all__"




# class UserSerializer(serializers.ModelSerializer):
#     billing_user=BillingSerializer()
    
#     class Meta:
#         model = User
#         fields = ["billing_user","id",]