from django.shortcuts import render, get_object_or_404,redirect,reverse
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_to_cart(request, product_id):

    #open file find the key 'shopping cart' in the session
    #if 'shopping cart' is not found return empty dict
    cart = request.session.get('shopping_cart', {})

    
    #The product not in the cart
    if product_id not in cart:
        product = get_object_or_404(Product, pk=product_id)
        cart[product_id] = {
            'id': product_id,
            'name': product.name,
            'cost': float(product.price),
            'each_cost': float(product.price),
            'qty': 1,
        }
        messages.success(request, f"Product:{product.name} has been added")

    #product already in cart
    else:
        cart[product_id]['qty'] += 1
        updated_qty= cart[product_id]['qty']
        OG_price = float(cart[product_id]['each_cost'])
        price = (OG_price*updated_qty)
        cart[product_id]['cost'] = str(price)

    #save the session
    request.session['shopping_cart'] = cart
    return redirect(reverse('show_cart_route'))


@login_required
def show_cart(request):
    #Get the session
    cart = request.session.get('shopping_cart')
    if cart:
        total_cart = 0
        for each_item in cart:
            each_item_cost = cart[each_item]['cost']
            total_cart += float(each_item_cost)

        
        return render(request, 'cart/show_cart.template.html',{
            'cart': cart,
            'total_cart': total_cart
            })
    else:
        return render(request, 'cart/empty_cart.template.html')

@login_required
def delete_from_cart(request, product_id):
    cart = request.session.get('shopping_cart')
    if product_id in cart:
        del cart[product_id]
        cart = request.session['shopping_cart']
        messages.success(request, "Item Deleted")
    return redirect(reverse('show_cart_route'))

@login_required
def update_quantity(request,product_id):
    cart = request.session.get('shopping_cart')
    if product_id in cart:
        cart[product_id]['qty'] = int(request.POST['qty'])

        newer_qty= int(request.POST['qty'])
        OG_price = float(cart[product_id]['each_cost'])
        update_price = (OG_price*newer_qty)
        cart[product_id]['cost'] = (update_price)
        request.session['shopping_cart'] = cart
        messages.success(request, f"Quantity has been updated")
    return redirect(reverse('show_cart_route'))
