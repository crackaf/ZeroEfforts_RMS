from django.forms import widgets
from django import forms
from .models import Sale
from inventory.models import Inventory

# class MyMultiSelect(widgets.SelectMultiple):
#     def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
#         option = super().create_option(name, value, label, selected, index, subindex, attrs)
#         option['attrs']['class'] = 'selectpicker'
#         return option

class SaleForm(forms.ModelForm):
    SOME_CHOICES = (
        (1, "Havana"),
        (2, "New York"),
        (3, "Changai"),
        (4, "London"),
    )
    # invetoryieess= forms.ModelMultipleChoiceField(Inventory.objects.all())
    inventories = forms.ModelMultipleChoiceField(
        queryset=Inventory.objects.all(),
        widget=forms.Select(attrs={
            'class': 'selectpicker'
        }
        )
    )
    
    # invent=forms.ModelMultipleChoiceField(
    #     queryset=Inventory.objects.all(),
    #     widget=MyMultiSelect
    # )
    

    class Meta:
        model = Sale
        fields = "__all__"
