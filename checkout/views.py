from django.shortcuts import render, get_object_or_404, reverse, HttpResponse, redirect
from django.conf import settings
from product.models import Product
from accounts.models import Order
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# endpoint_secret = settings.SIGNING_SECRET
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
    cart = request.session.get('shopping_cart',{})
    customer = User.objects.get(username=request.user)

    for id, product in cart.items():
        product_object = Product.objects.get(id=id)
        newproduct = Order(
            user=customer,
            product=product_object,
        )
        newproduct.save()

    request.session['shopping_cart'] = {}
    messages.success(request, f"Your Order has been place")

    return redirect(reverse('profile'))


def checkout_cancelled(request):
    return redirect(reverse('show_cart_route'))

@csrf_exempt
def handle_payment_completed(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header,settings.SIGNING_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    handle_checkout_session(session)

  return HttpResponse(status=200)

  def handle_checkout_session(session):
      print(session)
