from django.shortcuts import render, redirect
from category.models import *
from staticpage.models import *
from product.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.


class Products(APIView):

    def get(self, request):
        products=Product.objects.all()
        prod=ProductSerializers(products, many=True)
        return Response(prod.data)


class ProductDetailViews(APIView):
    def get(self, request, id):
        prodetail=Product.objects.get(id=id)
        detail=ProductDetailSerializers(prodetail)
        return Response(detail.data)





def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    c = Category.objects.get(id=1)
    a = c
    print(a)
    
    sliders = Slider.objects.all()
    #request.session['test'] = 10
    print(request.session.items())
    products = Product.objects.all()[:10]
    context = {
        'categories':categories,
        'sliders':sliders,
        'c': c,
        'products':products, 
    }
    return render(request,'index.html', context)
    
@csrf_exempt
def add_to_wishlist(request,id):
    if request.method == "POST":
        if not request.session.get('wishlist'):
            request.session['wishlist'] = list()
        else:
            request.session['wishlist'] = list(request.session['wishlist'])
        items = next((item for item in request.session['wishlist'] if item['id']==id),False)
    add_data = {
        'id':id,
    }
    if not items:
        request.session['wishlist'].append(add_data)
        request.session.modifier = True
    return redirect('index')

@csrf_exempt
def remove_wishlist(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        for i in request.session['wishlist']:
            if str(i['id']) == id:
                i.clear()
        while {} in request.session['wishlist']:
            request.session['wishlist'].remove({})
        if not request.session['wishlist']:
            del request.session['wishlist']
    try:
        request.session['wishlist'] = list(request.session['wishlist'])
    except:
        pass
    request.session.modifier = True
    return JsonResponse({'status':'ok'})


