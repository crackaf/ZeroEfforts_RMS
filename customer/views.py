from django.shortcuts import render
from .models import Customer
# Create your views here.

def customer(request):
    customers = Customer.objects.all()

    return render(request, 'customer/customers.html', {'customers': customers})
