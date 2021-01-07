"""Blog's admin configuration"""

# Django
from django.contrib import admin

# Models
from blogs.models import Category, Blog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin configuration."""

    readonly_fields=('id','created','updated')
    fields=('id','name','created','updated')
    list_display=('id','name','created','updated')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Blog admin configuration."""

    readonly_fields=('id','created','updated')
    fields=('id','title','content','image','author','category','created','updated')
    #list_display=('id','title','content','image','author','category','created','updated')