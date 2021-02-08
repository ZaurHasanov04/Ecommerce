from django.shortcuts import render
from category.models import Category

# Create your views here.

def category(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'category.html', context)

def category_products(request, slug):
    products = Category.products_in_category(slug)
    context = {
        'products':products
    }
    return render(request, 'category_products.html', context)