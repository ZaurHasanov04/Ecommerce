from django.db import models

# Create your models here.


class Slider(models.Model):
    url= models.URLField(max_length=200)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    