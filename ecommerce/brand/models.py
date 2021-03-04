from django.db import models
from utils.genslug import gen_slug
from django.urls import reverse

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    brand_slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.brand_slug:
            self.brand_slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def products_in_brand(brand_slug):
        brand = Brand.objects.get(brand_slug=brand_slug)
        return brand.product_set.all()

