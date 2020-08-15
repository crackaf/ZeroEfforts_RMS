from django import forms
from .models import Inventory
from store.models import Store


class InventoryForm(forms.ModelForm):
    store=forms.ModelChoiceField(Store.objects.all())
    class Meta:
        model = Inventory
        fields = "__all__"
        
