from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_to_wishlist/<int:id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_wishlist/', remove_wishlist, name='remove_wishlist'),
    path('api/product/', Products.as_view()),
    path('api/product/<int:id>', ProductDetailViews.as_view()),
]