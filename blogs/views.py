"""Blogs views."""

# Django
from django.shortcuts import render

# Models


def blogs(request):
    """Blogs view."""
    return render(request, "blogs/blogs.html")