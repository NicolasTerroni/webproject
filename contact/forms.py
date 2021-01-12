"""Contact forms."""

# Django
from django import forms


class ContactForm(forms.Form):
    """Contact form"""

    name=forms.CharField(label='Name',max_length=50, required=True)

    email=forms.EmailField(label='Email',required=True)

    content=forms.CharField(label='Content',widget=forms.Textarea,required=True)
