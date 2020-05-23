from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100,blank=False)
    content = models.TextField(blank=False)
    Posted_date = models.DateTimeField(blank=False,auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title