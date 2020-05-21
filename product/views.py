from django.shortcuts import render,HttpResponse,redirect,reverse,get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'product/index.template.html',{
        'product': product
    })

def create_product(request):
    if request.method == 'POST':
        create_form = ProductForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'product/create_product.template.html',{
                'form': create_form
            })

    else:
        create_form = ProductForm()
        return render(request, 'product/create_product.template.html',{
            'form': create_form
        })