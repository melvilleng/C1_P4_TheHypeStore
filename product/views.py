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

def update_product(request,product_id):
    update_product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form_for_product =ProductForm(request.POST,instance=update_product)
        if form_for_product.is_valid():
            form_for_product.save()
            return redirect(reverse(index))
        else:
            return render(request, 'product/update_product.template.html', {
                "form": form_for_product
                })
    else:
        form_for_product = ProductForm(instance=update_product)
        return render(request, 'product/update_product.template.html', {
            "form": form_for_product
        })

def delete_product(request,product_id):
    product_to_delete = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product_to_delete.delete()
        return redirect(index)

    else:
        return render(request, 'product/product_delete.template.html',{
            "product": product_to_delete
        })