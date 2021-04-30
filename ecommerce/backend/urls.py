from django.urls import path
from backend.views import *


urlpatterns=[
    path('api/user/', UserDetail.as_view()),
    path('api/token/', LoginTokenSerializers.as_view()),
    path('api/register', RegisterViews().as_view())
]