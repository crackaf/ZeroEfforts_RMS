from django import template
# from ..models import Inventory
from stock.models import Stock


register = template.Library()


@register.filter
def get_quantity(self, sep_store=False):
    if sep_store is False:
        qtyDicList = Stock.objects.filter(inventory=self).values('quantity')
        return sum([qty['quantity'] for qty in qtyDicList])
    else:
        return get_object_or_404(Stock, inventory=self, store=sep_store)
