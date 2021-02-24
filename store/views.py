"""Store app views"""

from django.shortcuts import render

def store(request):
    """Store view."""
    return render(request, "store/store.html")


