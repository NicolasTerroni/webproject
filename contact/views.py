"""Contact views"""

# Django
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
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

            email = EmailMessage(
                "Django app message",
                f"From: {name}\nEmail:{email}\n{content}",
                f"{email}",
                ("danieljoyas01@gmail.com",),
                reply_to=[email,]
                )
            
            try:
                email.send()
                return redirect("/contact/?valid")

            except:
                return redirect("/contact/?failed")
            
            
    else:
        contact_form = ContactForm()

    return render(request, "contact/contact.html", {'contact_form':contact_form})
