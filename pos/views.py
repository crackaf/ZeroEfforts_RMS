from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
# Create your views here.

class BrandObjectMixin(object):


    def get_object(self):
        id
    

class BrandCreateView(CreateView):
    template_name = 'pos/brand_create.html'
    form_class = BrandForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def base_view(request):
    return render(request, 'base.html')
