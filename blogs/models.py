"""Blogs models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Blog's categories model,"""

    name=models.CharField(max_length=50)
    
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Blog(models.Model):
    """Blog model."""

    title=models.CharField(max_length=30)
    content=models.CharField(max_length=150)
    image=models.ImageField(upload_to='blog',null=True,blank=True)

    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)

    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.title
