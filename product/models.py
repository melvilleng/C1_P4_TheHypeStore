from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=100)
    price = models.FloatField(blank=False)
    description = models.TextField(blank=False)
    size = models.CharField(blank=False,max_length=20)
    color = models.CharField(blank=False, max_length=50)
    image = ImageField(blank=True, manual_crop="")
    date = models.DateField(auto_now=False,auto_now_add=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.category_name