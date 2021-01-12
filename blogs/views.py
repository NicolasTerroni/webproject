"""Blogs views."""

# Django
from django.shortcuts import render

# Models
from blogs.models import Category, Blog


def blogs(request):
    """Blogs view."""
    
    blogs = Blog.objects.all()
    return render(request, "blogs/blogs.html", {'blogs':blogs})


def category(request,category_id):
    """Categories view."""
    
    category=Category.objects.get(id=category_id)
    blogs = Blog.objects.filter(categories=category)

    return render(request, "blogs/category.html", {'category':category,'blogs':blogs})