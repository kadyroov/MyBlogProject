from django import forms
from contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'phone', 'message', 'is_helium',
            'is_painted', 'is_foil', 'is_metallic'
        ]
        