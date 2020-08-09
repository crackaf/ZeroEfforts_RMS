from django.shortcuts import render
from .models import Inventory
# Create your views here.

def inventory(request):
    products= Inventory.objects.all()

    return render(request, 'inventory/inventory.html', {'products':products})