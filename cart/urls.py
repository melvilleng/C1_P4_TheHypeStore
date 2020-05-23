from django.urls import path
import cart.views

urlpatterns = [
    path('add_to_cart/<product_id>', cart.views.add_to_cart, name="add_to_cart_route"),
    path('show_cart/', cart.views.show_cart, name="show_cart_route"),
    # path('delete_from_cart/<product_id>', cart.views.delete_from_cart, name='delete_from_cart_route')
]