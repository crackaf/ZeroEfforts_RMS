from django.shortcuts import render, get_object_or_404
from .models import Manufacturer
# Create your views here.


def manufacturer(request):
    products = Manufacturer.objects.all()
    return render(request, 'manufacturer/manufacturer.html', {'products': products})


def manufacturerDetail(request, pk):
    product = get_object_or_404(Manufacturer, id=pk)
    return render(request, 'manufacturer/manufacturer_detail.html', {'product': product})
