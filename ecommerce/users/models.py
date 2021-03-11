from django.db import models

# Create your models here.

class Users(models.Model):
    firstname=models.CharField(max_length=50, null=True)
    lastname=models.CharField(max_length=50, null=True)
    email=models.EmailField(null=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    