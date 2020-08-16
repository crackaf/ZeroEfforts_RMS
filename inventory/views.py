from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory
from .forms import InventoryForm
from stock.forms import StockForm
from stock.models import Stock
# Create your views here.


def inventory(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory/inventory.html', {'items': inventories})


def inventoryCreate(request):
    form = InventoryForm()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            newInventory = form.save()
            print(form.cleaned_data['store'].pk,
                  newInventory.name,
                  form.cleaned_data['quantity'],
                  sep='\n'
            )
            newStock = Stock(
                store=form.cleaned_data['store'],
                inventory=newInventory,
                quantity=form.cleaned_data['quantity']
            )
            newStock.save()
            return redirect('inventory:inventory')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def inventoryDetail(request, pk):
    inventory = get_object_or_404(Inventory, id=pk)
    return render(request, 'inventory/inventory_detail.html', {'item': inventory})


def inventoryUpdate(request, pk):
    cust = get_object_or_404(Inventory, id=pk)
    form = InventoryForm(instance=cust)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def inventoryDelete(request, pk):
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
