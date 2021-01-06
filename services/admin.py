"""Services admin config"""

#Django
from django.contrib import admin

#Models
from services.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Service admin."""
    date_hierarchy = "created"
    readonly_fields=('id','created','updated')
    fields=('id','title','content','image','created','updated')
    list_display=('id','title','content','image','created','updated')
    list_display_links=('id','title')
    list_filter=('created','updated')
    search_fields=('id','title')
