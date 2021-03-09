"""Store app views"""

# Django
from django.shortcuts import render
# Models
from store.models import Product

def store(request):
    """Store view."""

    products = Product.objects.all()

    return render(request, "store/store.html",{'products':products})