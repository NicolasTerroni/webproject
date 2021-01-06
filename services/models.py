"""Services models."""

# Django
from django.db import models
from django.urls import reverse

class Service(models.Model):
    """Services model."""
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='services', height_field=None, width_field=None, max_length=None)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        """Service's metadata."""
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

"""    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})"""
