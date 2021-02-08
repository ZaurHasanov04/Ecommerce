from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from category.models import Category
from utils.genslug import gen_slug
from django.urls import reverse

# Create your models here.

def upload_product_file_loc(instance,filename):
    if instance.__class__ == ProductFile :
        slug = instance.product.slug
    else :
        slug = instance.slug
    id_  = instance.id # print edende birce id gelir, _ isaresini qoymanin menasi tam olaraq nedirki?
    print(id_)
    if id_ is None: # None olmadigi hal var olan obyekti edit etme hali ucundur?
        Klass = instance.__class__
        qs = Klass.objects.all().order_by('-pk')
        print(qs)
        if qs.exists():
            id_ = qs.first().id + 1
        else:
            id_ = 0
    if not slug:
        slug = gen_slug(instance.product)
    location = "product/{slug}/{id}/".format(slug=slug, id=id_)
    return location + filename


class Product(models.Model):
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(blank=True)
    product_name = models.CharField(max_length=50,blank=True,null=True)
    product_descrption = models.TextField(blank=True,null=True)
    product_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    product_discount = models.DecimalField(max_digits=9,decimal_places=1,blank=True,null=True)
    product_discount_price =  models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    product_image = models.ImageField(
        upload_to=upload_product_file_loc,
        storage=FileSystemStorage(location=settings.MEDIA_ROOT), 
        blank=True,
        null=True
    )
    product_stock = models.BooleanField(default=False)
    product_title = models.TextField(blank=True,null=True)
    product_vip = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.product_name)

        if self.product_discount >= 1: # burda error var ki, nonetype ile int arasi >= emeliyyati aparaila bilmez
            change = float(self.product_price) * float(self.product_discount) / 100
            self.product_discount_price = float(self.product_price) - change
        super().save(*args, **kwargs)

    def get_downloads(self):
        qs = self.productfile_set.all()
        return qs


class ProductFile(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    file = models.FileField(
        upload_to=upload_product_file_loc,
        storage=FileSystemStorage(location=settings.PRODUCT_STOREGE)
    )