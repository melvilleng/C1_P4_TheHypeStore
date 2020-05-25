from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = ImageField(blank=True, manual_crop="")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.category_name

class Size(models.Model):
    size_option =(
        ('XS','Extra-Small'),
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra-Large')

    )
    sizes = models.CharField(max_length=150, choices=size_option)
    product = models.ManyToManyField(Product, related_name='sizes')

    def __str__(self):
        return self.sizes