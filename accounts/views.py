from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

def profile(request):

    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile/profile.template.html',{
            "userprofile": userprofile
        })
