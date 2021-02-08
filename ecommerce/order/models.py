from django.db import models
# from billing.models import BillingProfile
from cart.models import Cart
import datetime
import time
# Create your models here.

ORDER_CHOICES_STATUS=[
    ('PAID','PAID'),
    ('SHIPPED','SHIPPED'),
    ('DELIVERED', 'DELIVERED')
]



class Order(models.Model):
    order_cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_timestamp=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(max_length=20, choices=ORDER_CHOICES_STATUS)




