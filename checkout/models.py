import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from product.models import Product



# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=50, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    zipcode = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=255, blank=False)
    address_2 = models.CharField(max_length=150, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def _generate_order_number(self):

        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        self.order_total = self.lineitems.aggretate(Sum('lineitem_total'))['lineitem_total_sum']
        self.grand_total = self.order_total
        self.save()

    def save(self, *args,**kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,blank=False,on_delete=models.CASCADE,related_name='lineitems')
    product = models.ForeignKey(Product, blank=False,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False,default=0)
    lineitem_total = models.DecimalField(max_digits=10,decimal_places=2,blank=False,editable= False)

    
    def save(self, *args,**kwargs):
        
        self.lineitem_total = self.product.cost * self.quantity
        super().save(*args,**kwargs)