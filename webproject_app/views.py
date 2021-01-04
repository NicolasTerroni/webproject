"""Webproject_app views."""

# Django
from django.shortcuts import render, HttpResponse


def home(request):
    """Home view."""
    return render(request, "webproject_app/home.html")


def services(request):
    """Services view."""
    return render(request, "webproject_app/services.html")


def store(request):
    """Store view."""
    return render(request, "webproject_app/store.html")


def blogs(request):
    """Blogs view."""
    return render(request, "webproject_app/blogs.html")


def contact(request):
    """Contact view."""
    return render(request, "webproject_app/contact.html")

