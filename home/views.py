from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def create(request):
    return render(request, 'create.html')
