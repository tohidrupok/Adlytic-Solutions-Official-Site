from django import forms
from .models import PackageOrder

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PackageOrder
        fields = ['package', 'name', 'contact', 'email', 'address']
        widgets = {
            'package': forms.HiddenInput()  # Hide kore rakchi
        }

