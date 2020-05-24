from django.contrib import admin
from django.urls import path, include
import reviews.views


urlpatterns = [
    path('show_review/', reviews.views.show_review, name='show_reviews_route'),
    path('reviews/create_review', reviews.views.create_review)
    
]