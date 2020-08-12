from django.shortcuts import render
from .models import Customer
# Create your views here.


def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customers.html', {'customers': customers})

def customerCreate(request):
    pass

def customerDetail(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    return render(request, 'customer/customer_detail.html', {'customer': customer})


def customerUpdate(request, pk):
    pass


def customerDelete(request, pk):
    pass


