from django import forms
from .models import Product, Category
from pyuploadcare.dj.forms import ImageField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'image','category'

class SearchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=False)