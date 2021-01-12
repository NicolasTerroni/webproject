"""Contact views"""

# Django
from django.shortcuts import render, redirect
# Forms
from contact.forms import ContactForm

def contact(request):
    """Contact view."""
    if request.method == "POST":

        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")
            
            return redirect("/contact/?valid")
    else:
        contact_form = ContactForm()

    return render(request, "contact/contact.html", {'contact_form':contact_form})
