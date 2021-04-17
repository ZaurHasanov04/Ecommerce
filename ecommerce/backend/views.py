from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from backend.models import User
# Create your views here.

class UserDetail(APIView):
    def get(self, request):
        user=User.objects.filter(id=self.request.user.id)
        serializers=UserSerializer(user,many=True)
        
        return Response(serializers.data)
