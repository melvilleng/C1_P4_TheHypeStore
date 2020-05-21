from django.shortcuts import render,HttpResponse,redirect,reverse,get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'product/index.template.html',{
        'product': product
    })