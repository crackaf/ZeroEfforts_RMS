from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm
# Create your views here.


def category(request):
    categories = Category.objects.all()
    return render(request, 'category/category.html', {'items': categories})


def categoryCreate(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category:category')

    context = {
        'name': 'Add Category',
        'form': form,
    }
    return render(request, 'form_snippet.html', context)


def categoryDetail(request, pk):
    category = get_object_or_404(Category, id=pk)
    return render(request, 'category/category_detail.html', {'item': category})


def categoryUpdate(request, pk):
    categories = get_object_or_404(Category, id=pk)
    form = CategoryForm(instance=categories)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=categories)
        if form.is_valid():
            form.save()
            return redirect('category:category')

    context = {
        'name': 'Edit Category',
        'form': form,
    }
    return render(request, 'form_snippet.html', context)


def categoryDelete(request, pk):
    categories = get_object_or_404(Category, id=pk)
    if request.method == "POST":
        categories.delete()
        return redirect('category:category')

    context = {
        'item': categories,
        'delete_url': 'category:category-delete',
        'return_url': 'category:category'
    }
    return render(request, 'delete_snippet.html', context)
