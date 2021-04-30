from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from backend.models import User
from order.models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import TokenPairSerializers, RegisterSerializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework import generics
# Create your views here.


class LoginTokenSerializers(TokenObtainPairView):
    serializers_class=TokenPairSerializers()



class RegisterViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers




    
        



class UserDetail(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        order=Order.objects.filter(billing_profile_id=self.request.user.billing_user.id)
        serializers=OrderSerializer(order,many=True)
        return Response(serializers.data)
