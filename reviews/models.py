from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=150,blank=False)
    content = models.TextField(blank=False)
    posted_date = models.DateTimeField(blank=False, auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

