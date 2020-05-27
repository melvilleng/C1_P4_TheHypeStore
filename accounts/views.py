from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile,Order
from product.models import Product

# Create your views here.

def profile(request):

    userprofile = UserProfile.objects.get(user=request.user)
    product = Order.objects.filter(user=userprofile.user)
    return render(request, 'profile/profile.template.html',{
            "userprofile": userprofile,
            'product': product
        })

# def view_order(request):

#     customer = User.objects.get(username=request.user)

#     product = Order.objects.filter(username=customer)

#     return render(request, 'profile/profile.template.html',{
#         'product': product,
#         'customer': customer
#     })