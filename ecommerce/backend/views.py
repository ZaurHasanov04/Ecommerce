from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from backend.models import User
from order.models import Order
from rest_framework.permissions import IsAuthenticated
# from .serializers import TokenPairSerializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
# Create your views here.


# class LoginTokenSerializers(TokenObtainPairView):
#     serializers_class=TokenPairSerializers()



# class RegisterSerializers(serializers.ModelSerializer):
#     email=serializers.CharField()


class UserDetail(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self, request):
        order=Order.objects.filter(billing_profile_id=self.request.user.billing_user.id)
        serializers=OrderSerializer(order,many=True)
        
        return Response(serializers.data)
