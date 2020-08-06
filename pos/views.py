from django.shortcuts import render
from . import models
from django.views.generic.edit import CreateView
# Create your views here.

class BrandCreateView(CreateView):
    model = models.Brand
    template_name = "pos/brand.html"

    class ModelListView(ListView):
        model = Model
        template_name = ".html"
    


def base_view(request):
    return render(request, 'base.html')
