"""Webproject_app views."""

# Django
from django.shortcuts import render


def home(request):
    """Home view."""
    return render(request, "webproject_app/home.html")
