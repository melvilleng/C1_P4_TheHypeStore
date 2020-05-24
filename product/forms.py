from django import forms
from .models import Product, Category
from pyuploadcare.dj.forms import ImageField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'image', 'size', 'color','date','category'

class SearchForm(forms.Form):
    name = forms.CharField(max_length=150, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=False)