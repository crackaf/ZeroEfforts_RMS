from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from .forms import SaleForm
# Create your views here.


def sale(request):
    sales = Sale.objects.all()
    return render(request, 'sale/sale.html', {'items': sales})

def saleCreate(request):
    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale:sale')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def saleDetail(request, pk):
    sale = get_object_or_404(Sale, id=pk)
    return render(request, 'sale/sale_detail.html', {'item': sale})


def saleUpdate(request, pk):
    cust = get_object_or_404(Sale, id=pk)
    form = SaleForm(instance=cust)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('sale:sale')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def saleDelete(request, pk):
    cust = get_object_or_404(Sale, id=pk)
    if request.method == "POST":
        cust.delete()
        return redirect('sale:sale')

    context = {
        'item': cust,
        'delete_url': 'sale:sale-delete',
        'return_url': 'sale:sale'
    }
    return render(request, 'delete_snippet.html', context)
