from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
from product.models import Product

# Create your views here.

def profile(request):

    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile/profile.template.html',{
            "userprofile": userprofile
        })

def view_order(request):

    customer = UserProfile.objects.get(user=request.user)

    product = Product.objects.filter(user=customer)

    return render(request, 'profile/profile.template.html',{
        'product': product
    })