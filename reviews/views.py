from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ReviewForm
from product.models import Product
from reviews.models import Review
from django.contrib import messages

# Create your views here.
def show_review(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/show_review.template.html',{
        'reviews': reviews
    })
