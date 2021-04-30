from rest_framework import serializers
from billing.models import BillingProfile
from order.models import Order
from backend.models import User
from cart.models import Cart, CartProduct
from product.models import Product
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenPairSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token=super(TokenPairSerializers,cls).save(user)

        token['username']=user.username

        return token


class RegisterSerializers(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2=serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password", "password2",]
        extra_kwargs={
            "first_name":{"required":True},
            "last_name":{"required":True},
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Sifre tekrari sehvdir."})
        return attrs

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



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