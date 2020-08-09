from django.shortcuts import render
from .models import Customer
# Create your views here.


def customer(request):
    customers = Customer.objects.all()

    return render(request, 'customer/customers.html', {'customers': customers})

def customerDetail(request, pk):
    customer = Customer.objects.get(id=pk)

    return render(request, 'customer/customer_detail.html', {'customer': customer})
