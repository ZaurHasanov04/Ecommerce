from rest_framework import serializers
from product.models import Product
from brand.models import Brand


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name',]

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class ProductDetailSerializers(serializers.ModelSerializer):
    product_brand = BrandSerializers(read_only=True)
    class Meta:
        model = Product
        fields = '__all__' 

