"""Product admin configuration"""

# Django
from django.contrib import admin
# Models
from store.models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("id","created_at","updated_at")

    list_display = (    "id",
                        "name",
                        "categories",
                        "image",
                        "price",
                        "aviable",
                        "created_at",
                        "updated_at")

    search_fields = ("id","name")
    list_filter = ("categories","aviable","created_at","updated_at")

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")