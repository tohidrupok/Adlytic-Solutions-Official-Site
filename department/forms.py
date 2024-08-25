from django import forms
from .models import PackageOrder, Contact

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PackageOrder
        fields = ['package', 'name', 'contact', 'email', 'address']
        widgets = {
            'package': forms.HiddenInput()  # Hide kore rakchi
        } 


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']