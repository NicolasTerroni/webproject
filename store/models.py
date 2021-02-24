"""Store app models"""

# Django
from django.db import models


class ProductCategory(models.Model):
    """Product's categories model"""
    
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.name
    


class Product(models.Model):
    """Product's model"""

    name = models.CharField(max_length=100)
    categories = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="store", null=True, blank=True)
    price = models.FloatField()
    aviable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"