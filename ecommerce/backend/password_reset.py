from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.serializers import *
from backend.models import *
from django.core.mail import send_mail
from django.core.management import settings
from django.shortcuts import render, redirect



class PasswordResetEmail(APIView):
    serializer_class = EmailSerializers

    def post(self, request):
        serializers=self.serializer_class(data=request.data)
        print(request.data)
        serializers.is_valid(raise_exception=True)
        email=serializers.validated_data['email']
        check_user=User.objects.filter(email=email)

        if check_user.count() > 0:
            get_user=User.objects.get(email=email)
            creates_verify = UserVerify.objects.get_or_create(user_id=get_user.id)
            subject="REset ucun"
            message="Asagidaki linke daxil olun \n\n http://127.0.0.1:8000/check_email/?token={}".format(creates_verify[0].token)
            receiver="{}".format(get_user.email)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [receiver], fail_silently=True)
            return Response({'success':'email gonderildi'})
        return Response({'data':'none'})


def check_email(request):
    if request.method=="GET":
        token=request.GET.get('token')
        try:
            check_token=UserVerify.objects.get(token=token)
            return redirect("http://127.0.0.1:8000/password_reset/?token=" + f"{check_token.token}")
        except:
            return JsonResponse({'error':"invalid token"})
    return JsonResponse({'data':'None'})


class PasswordReset(APIView):
    serializer_class=PasswordResetSerializers

    def post(self,request):
        serializers=self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        token = request.GET.get('token')
        user_verify=UserVerify.objects.get(token=token)
        get_user=User.objects.get(id=user_verify.user.id)
        get_user.set_password(serializers.validated_data['password'])
        get_user.save()
        user_verify.delete()
        return Response({'Sifre':'Sifre deyisdirildi'})

