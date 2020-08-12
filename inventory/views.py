from django.shortcuts import render, get_object_or_404
from .models import Inventory
# Create your views here.

def inventory(request):
    products = Inventory.objects.all()
    return render(request, 'inventory/inventory.html', {'products':products})

def inventoryDetail(request, pk):
    product = get_object_or_404(Inventory, id=pk)
    return render(request, 'inventory/inventory_detail.html', {'product': product})
