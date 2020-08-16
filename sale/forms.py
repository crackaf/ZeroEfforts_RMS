from django import forms
from .models import Sale
from inventory.models import Inventory


class SaleForm(forms.ModelForm):
    SOME_CHOICES = (
        (1, "Havana"),
        (2, "New York"),
        (3, "Changai"),
        (4, "London"),
    )

    inventories = forms.ModelChoiceField(queryset=Inventory.objects.all(),
                                         widget=forms.SelectMultiple(
        attrs={
            'class': 'selectpicker'
        }
    )
    )
    testing2 = forms.ModelMultipleChoiceField(queryset=Inventory.objects.all(),
                                              widget=forms.SelectMultiple(attrs={
                                                  'class': 'selectpicker'
                                              }
    )
    )

    class Meta:
        model = Sale
        fields = "__all__"


class CustomerForm(forms.Form):

    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
