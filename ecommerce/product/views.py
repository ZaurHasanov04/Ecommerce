from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# from django.views.generic import DetailView
# from analytics.mixins import ObjectViewedMixin
# from cart.models import Cart

# Create your views here.

def product_detail(request, slug):
    product_detail = get_object_or_404(Product, slug=slug)
    context = {
        "product_detail":product_detail
    }
    return render(request, 'product_detail.html', context)



# class ProductDetail(ObjectViewedMixin, DetailView):
#     queryset = Product.objects.all()
#     template_name = 'products/product.html'

#     def get_context_data(self, **kwargs):
#         context = super(ProductDetail, self).get_context_data(**kwargs)
#         context["cart"] = 'okey' # niye 'okey' yazmisiq bura?)
#         return context
    
#     def get_object(self, *args, **kwargs):
#         request = self.request
#         id = self.kwargs.get('id')
#         instance = Product.objects.get(id=id)
#         return instance


def product(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'user': request.user
    }
    return render(request, 'products/product.html', context)