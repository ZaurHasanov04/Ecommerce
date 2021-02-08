from django.db import models
from backend.models import User
from product.models import Product
from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from decimal import Decimal

# Create your models here.

class CartMeneger(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None) 
        qs = self.get_queryset().filter(id=cart_id) # self yerine super() yaza bilerdikmi?
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_id.id
        return cart_obj , new_obj
# burda hardan yoxlaya bilir ki, basqa hansisa cart item-larin birinde produclarinda burda
# secilen productlar eynidi ya ferqlidi? mence qs ucun filterleme productlara gore edilmelidi(line 10)
# elaveten user terefi aydin olmur tam olaraq, mence algoritmik typo var kodda:DD

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    # mence user ile cart many_to_many relation olmalidi
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField(Product,related_name='cart_products')
    subtotal = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    object = CartMeneger()

    def __str__(self):
        return str(self.id)


@receiver(m2m_changed, sender=Cart.products.through)
def m2m_changed_cart_reciver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products :
            if x.product_discount_price :
                total += x.product_discount_price
            else :
                total += x.product_price # mence discount price-i varsa, onu elave etmek lazimdi
        if instance.subtotal != total :
            instance.subtotal = total
            # run functions pre_save_cart_receiver
            instance.save()


@receiver(pre_save, sender=Cart)
def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0 :
        instance.total = Decimal(instance.subtotal) * Decimal(settings.SUB_TOTAL_PERCENTAGE)
    else :
        instance.total = 0.00

