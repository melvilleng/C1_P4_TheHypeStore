"""thehypestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', product.views.index, name='show_product_route'),
    path('product/create_product',product.views.create_product),
    path('product/update_product/<product_id>',product.views.update_product, name='update_product_route'),
    path('product/delete_product/<product_id>',product.views.delete_product, name= 'delete_product_route'),
]
