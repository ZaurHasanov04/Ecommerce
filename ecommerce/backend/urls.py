from django.urls import path
from .views import *


urlpatterns=[
    path('api/user/', UserDetail.as_view())
]