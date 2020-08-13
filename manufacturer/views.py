from django.shortcuts import render, redirect, get_object_or_404
from .models import Manufacturer
from .forms import ManufacturerForm
# Create your views here.


def manufacturer(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer/manufacturer.html', {'items': manufacturers})


def manufacturerCreate(request):
    form = ManufacturerForm()
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturer:manufacturer')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def manufacturerDetail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, id=pk)
    return render(request, 'manufacturer/manufacturer_detail.html', {'item': manufacturer})


def manufacturerUpdate(request, pk):
    manufacturers = get_object_or_404(Manufacturer, id=pk)
    form = ManufacturerForm(instance=manufacturers)
    if request.method == 'POST':
        form = ManufacturerForm(request.POST, instance=manufacturers)
        if form.is_valid():
            form.save()
            return redirect('manufacturer:manufacturer')

    context = {'form': form}
    return render(request, 'form_snippet.html', context)


def manufacturerDelete(request, pk):
    manufacturers = get_object_or_404(Manufacturer, id=pk)
    if request.method == "POST":
        manufacturers.delete()
        return redirect('manufacturer:manufacturer')

    context = {
        'item': manufacturers,
        'delete_url': 'manufacturer:manufacturer-delete',
        'return_url': 'manufacturer:manufacturer'
    }
    return render(request, 'delete_snippet.html', context)
