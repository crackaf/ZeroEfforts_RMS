from django import forms
from . import models

class BrandForm(forms.ModelForm):
    
    class Meta:
        model = Brand
        fields = ("",)

