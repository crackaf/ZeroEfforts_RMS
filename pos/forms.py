from django import forms
from . import models

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ("__all__")

    widgets={
        'name' : forms.TextInput( attrs={
                'class' : 'yourclass example'
        }
        )
        
    }