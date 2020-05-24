from django.contrib import admin
from django.urls import path, include
import reviews.views


urlpatterns = [
    path('show_review/', reviews.views.show_review, name='show_reviews_route'),
    path('reviews/create_review/<product_id>', reviews.views.create_review, name='create_review_route')
    
]