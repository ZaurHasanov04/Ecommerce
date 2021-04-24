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


class ProductPrice(serializers.Field):
    def to_representation(self, value):
        data_price={
            "Mehsulun Qiymeti":value.product_price,
            "Endirim Faizi": value.product_discount,
            "Endirimli Qiymeti" : value.product_discount_price
        }
        return data_price


class ProductSerializers(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    price=ProductPrice(source="*")
    class Meta:
        model = Product
        exclude = ['product_price','product_discount', 'product_discount_price',]

    def get_category(self, obj):
        cat=obj.product_brand.sub_category.category.name
        ids=obj.product_brand.sub_category.category.id
        
        data={
            "id":ids,
            "Category":cat
        }
        

        return data


class ProductDetailSerializers(serializers.ModelSerializer):
    product_brand = BrandSerializers(read_only=True)
    productfile_set = ProductFileSerializers(many=True)
    class Meta:
        model = Product
        fields = '__all__' 

