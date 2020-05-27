from django.shortcuts import render,get_object_or_404,reverse,HttpResponse
from django.conf import settings
from product.models import Product
from django.contrib.sites.models import Site
import stripe


# Create your views here.

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    #generate line items
    line_items = []

    cart = request.session.get('shopping_cart',{})

    for id, product in cart.items():
        product_from_db = get_object_or_404(Product, pk=id)
        line_item = {
            'name': product_from_db.name,
            'amount': int(product_from_db.price*100),
            'currency': 'sgd',
            'quantity': product['qty']
        }
        line_items.append(line_item)
    
    current_site = Site.objects.get_current()
    domain = current_site.domain
    
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        success_url=domain + reverse(checkout_success),
        cancel_url=domain + reverse(checkout_cancelled),
    )

    return render(request, 'checkout/checkout.template.html',{
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })

def checkout_success(request):
    # reset the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout successful")


def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")