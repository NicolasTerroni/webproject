
# Django
from django.shortcuts import render


# Models
from services.models import Service

def services(request):
    """Services view."""
    services=Service.objects.all()
    return render(request, "services/services.html",{'services':services})