from django.shortcuts import render, redirect, get_object_or_404
from .models import Address
from .forms import AddressForm
# Create your views here.


def address(request):
    addresses = Address.objects.all()
    return render(request, 'address/address.html', {'items': addresses})


def addressCreate(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address:address')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def addressDetail(request, pk):
    address = get_object_or_404(Address, id=pk)
    return render(request, 'address/address_detail.html', {'item': address})


def addressUpdate(request, pk):
    cust = get_object_or_404(Address, id=pk)
    form = AddressForm(instance=cust)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('address:address')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def addressDelete(request, pk):
    cust = get_object_or_404(Address, id=pk)
    if request.method == "POST":
        cust.delete()
        return redirect('address:address')

    context = {
        'item': cust,
        'delete_url': 'address:address-delete',
        'return_url': 'address:address'
    }
    return render(request, 'delete_snippet.html', context)
