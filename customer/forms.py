from django.forms import ModelForm


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ("__all__",)
