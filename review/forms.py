from django import forms
from .models import Review

class Review(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','content','posted_date','product')