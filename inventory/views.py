from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory
from .forms import InventoryForm
# Create your views here.


def inventory(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory/inventory.html', {'items': inventories})


def customerCreate(request):
    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def customerDetail(request, pk):
    inventory = get_object_or_404(Inventory, id=pk)
    return render(request, 'inventory/inventory_detail.html', {'item': inventory})


def customerUpdate(request, pk):
    cust = get_object_or_404(Inventory, id=pk)
    form = InventoryForm(instance=cust)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def customerDelete(request, pk):
    cust = get_object_or_404(Inventory, id=pk)
    if request.method == "POST":
        cust.delete()
        return redirect('inventory:inventory')

    context = {
        'item': cust,
        'delete_url': 'inventory:inventory-delete',
        'return_url': 'inventory:inventory'
    }
    return render(request, 'delete_snippet.html', context)
