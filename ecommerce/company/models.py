from django.db import models
from product.models import Product
# Create your models here.

class Company(models.Model):
    product_id=models.ManyToManyField(Product)
    timestamp= models.DateTimeField(auto_now_add=True)