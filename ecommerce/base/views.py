from django.shortcuts import render
from category.models import Category, SubCategory
from staticpage.models import Slider

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    slider = Slider.objects.all()

    context = {
        'categories':categories,
        'slider':slider
    }
    return render(request,'index.html',context)


# def Subcategory_brand(request):
#     brands = SubCategory.objects.prefetch_related('subcategory_brands').all()
#     context = {
#         'brands':brands
#     }
#     return render(request, 'index.html', context)

