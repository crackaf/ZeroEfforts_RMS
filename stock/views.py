from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .forms import StockForm
# Create your views here.


def stock(request):
    stocks = Stock.objects.all()
    return render(request, 'stock/stock.html', {'items': stocks})


def stockCreate(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock:stock')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def stockDetail(request, pk):
    stock = get_object_or_404(Stock, id=pk)
    return render(request, 'stock/stock_detail.html', {'item': stock})


def stockUpdate(request, pk):
    cust = get_object_or_404(Stock, id=pk)
    form = StockForm(instance=cust)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('stock:stock')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def stockDelete(request, pk):
    cust = get_object_or_404(Stock, id=pk)
    if request.method == "POST":
        cust.delete()
        return redirect('stock:stock')

    context = {
        'item': cust,
        'delete_url': 'stock:stock-delete',
        'return_url': 'stock:stock'
    }
    return render(request, 'delete_snippet.html', context)
