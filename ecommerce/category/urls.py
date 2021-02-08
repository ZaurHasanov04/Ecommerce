from django.urls import path
from .views import *

urlpatterns = [
    path('', category, name='category'),
    path('category/<slug>/', category_products, name='category_products'),
]
