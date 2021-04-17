from rest_framework import serializers
from product.models import *
from brand.models import Brand
from category.models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class SubcategorySerializers(serializers.ModelSerializer):
    category=CategorySerializers(read_only=True)
    class Meta:
        model= SubCategory
        fields="__all__"


class BrandSerializers(serializers.ModelSerializer):
    sub_category= SubcategorySerializers()
    class Meta:
        model = Brand
        exclude = ['brand_slug',]


class ProductFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        exclude = ['product',]

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class ProductDetailSerializers(serializers.ModelSerializer):
    product_brand = BrandSerializers(read_only=True)
    productfile_set = ProductFileSerializers(many=True)
    class Meta:
        model = Product
        fields = '__all__' 

