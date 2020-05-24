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

def create_review(request):
    if request.method == "POST":
        create_review_form = ReviewForm(request.POST)
        review = create_review_form.save(commit=False)
        review.user = request.user
        review.save()
        messages.success(request, "Review Added")
        return redirect(reverse(show_review))
    else:
        create_review_form = ReviewForm()

    return render(request, 'reviews/create_review.template.html',{
        'form': create_review_form
    })