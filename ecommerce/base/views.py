from django.shortcuts import render
from category.models import Category, SubCategory

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    context = {
        'categories':categories,
    }
    return render(request,'index.html',context)


def Subcategory_brand(request):
    brands = SubCategory.objects.prefetch_related('subcategory_brands').all()
    context = {
        'brands':brands
    }
    return render(request, 'index.html', context)
