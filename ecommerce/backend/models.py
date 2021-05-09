from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from datetime import datetime, timedelta
from django.core.management import settings
# Create your models here.

class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    is_branch = models.BooleanField(default=True)
    is_delivery = models.BooleanField(default=True)
    is_phone_status = models.BooleanField(default=False)


class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address_name = models.CharField(max_length=40)
    home = models.CharField(max_length=10)
    city = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class UserOtp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_otp')
    otp = models.CharField(max_length=6)
    rpt = models.IntegerField(default=3)
    date = models.DateTimeField(auto_now=True)
    

class UserVerify(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=400, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.token
    def save(self, *args, **kwargs):
        self.token=''
        if not self.token:
            self.token=self._create_verify()
        super().save(*args,**kwargs)
    def _create_verify(self):
        dt=datetime.now() + timedelta(days=60)
        hashing= jwt.encode({
            'id': self.id,
            'exp':int(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return hashing

    