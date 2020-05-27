from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class UserProfile(models.Model):
    address = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=60,blank=False)
    zipcode = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=100,blank=False)
    contact = models.PositiveIntegerField(blank=False)
    user =models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "UserProfile" + str(self.id)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "Order" + str(self.id)
    
