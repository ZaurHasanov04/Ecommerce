from django.urls import path
from .views import *

urlpatterns = [
    path('category/product/<slug>/', product_detail, name='product_detail'),
    # path('<int:id>/', ProductDetail.as_view(), name='product_detail')
]
