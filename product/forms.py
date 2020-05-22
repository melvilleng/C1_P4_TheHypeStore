from django import forms
from .models import Product
from pyuploadcare.dj.forms import ImageField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'image', 'size', 'color','date','category'