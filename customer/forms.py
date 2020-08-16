from django import forms
from .models import Customer

# class CustomerForm(forms.ModelForm):
    
#     class Meta:
#         model = Customer
#         fields = "__all__"
    

class CustomerForm(forms.Form):

    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
