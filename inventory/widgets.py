"""
https://stackoverflow.com/questions/5089396/django-form-field-choices-adding-an-attribute/56097149#56097149

Usage Example:
    colors = forms.MultipleChoiceField(
        label="Colors",
        choices=choices,
        widget=Select2MultipleWidgetWOA(
            attrs={'data-placeholder': 'Any color',
                'data-close-on-select': 'false',
                'style': 'width:280px; height:36px;',
                'title': 'Type a word to filter the menu',}
        )
    )
"""


from django_select2.forms import Select2Mixin
from django.forms.widgets import Select, SelectMultiple


class SelectWOA(Select):
    """
    Select With Option Attributes:
        subclass of Django's Select widget that allows attributes in options, 
        like disabled="disabled", title="help text", class="some classes",
              style="background: color;"...

    Pass a dict instead of a string for its label:
        choices = [ ('value_1', 'label_1'),
                    ...
                    ('value_k', {'label': 'label_k', 'foo': 'bar', ...}),
                    ... ]
    The option k will be rendered as:
        <option value="value_k" foo="bar" ...>label_k</option>
    """

    def create_option(self, name, value, label, selected, index,
                      subindex=None, attrs=None):
        if isinstance(label, dict):
            opt_attrs = label.copy()
            label = opt_attrs.pop('label')
        else:
            opt_attrs = {}
        option_dict = super(SelectWOA, self).create_option(name, value,
                                                           label, selected, index, subindex=subindex, attrs=attrs)
        for key, val in opt_attrs.items():
            option_dict['attrs'][key] = val
        return option_dict


class SelectMultipleWOA(SelectWOA, SelectMultiple):
    """ 
    SelectMultipleWOA widget works like SelectMultiple, with options attrs.
    See SelectWOA.
    """
    pass


class Select2MultipleWidgetWOA(Select2Mixin, SelectMultipleWOA):
    """
    Select2 drop in widget for multiple select.
    Works just like Select2MultipleWidget but with options attrs.
    """
    pass

