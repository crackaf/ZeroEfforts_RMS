from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '322f'}),
        'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '322f'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '322f'})
    }
