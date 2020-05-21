from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=100)
    price = models.FloatField(blank=False)
    description = models.TextField(blank=False)
    size = models.CharField(blank=False,max_length=20)
    color = models.CharField(blank=False, max_length=50)
    image = models.ImageField(blank=False)
    date = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name