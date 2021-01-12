"""Webproject_app views."""

# Django
from django.shortcuts import render, HttpResponse


def home(request):
    """Home view."""
    return render(request, "webproject_app/home.html")


def store(request):
    """Store view."""
    return render(request, "webproject_app/store.html")


