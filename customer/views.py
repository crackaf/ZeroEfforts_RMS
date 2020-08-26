from django.shortcuts import render, redirect, get_object_or_404
from address.models import Address
from .models import Customer
from .forms import CustomerForm
# Create your views here.


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer.html', {'items': customers})


def customerCreate(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:customer')

    context = {
        'name':'Add Customer',
        'form':form,
    }
    return render(request, 'form_snippet.html', context)


def customerDetail(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    return render(request, 'customer/customer_detail.html', {'item': customer})


def customerUpdate(request, pk):
    cust = get_object_or_404(Customer, id=pk)
    form = CustomerForm(instance=cust)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('customer:customer')

    context = {
        'name': 'Edit Customer',
        'form': form,
    }
    return render(request, 'form_snippet.html', context)


def customerDelete(request, pk):
    cust = get_object_or_404(Customer, id=pk)
    if request.method == "POST":
        cust.delete()
        return redirect('customer:customer')

    context = {
        'item': cust,
        'delete_url': 'customer:customer-delete',
        'return_url': 'customer:customer'
    }
    return render(request, 'delete_snippet.html', context)
