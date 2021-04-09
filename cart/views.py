"""Webproject views"""

# Django
from django.shortcuts import redirect
# Cart
from .cart import Cart
# Models
from store.models import Product

def add_product(request,product_id):
    """Add product to cart view."""

    cart = Cart(request)
    product = Product.objects.get(id=product_id)

    cart.add_product(product=product)
    
    return redirect('store')


def delete_product(request,product_id):
    """Add product to cart view."""

    cart = Cart(request)
    product = Product.objects.get(id=product_id)

    cart.delete_product(product=product)
    
    return redirect('store')


def substract_product(request,product_id):
    """Add product to cart view."""

    cart = Cart(request)
    product = Product.objects.get(id=product_id)

    cart.substract_product(product=product)
    
    return redirect('store')


def empty_cart(request):
    """Add product to cart view."""

    cart = Cart(request)
    cart.empty_cart()
    
    return redirect('store')