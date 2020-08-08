from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def index(request):
    if request.user.is_anonymous:
        return render(request, 'account/login.html')
    else:
        return render(request, 'account/index.html')


def login(request):
    if request.user.is_anonymous:
        return render(request, 'account/login.html')
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"))
        if user is not None:
            # A backend authenticated the credentials
            print(user.password)
            return render(request, 'account/index.html')
    return render(request, 'account/login.html')


def logout(request):
    logout(request)
    return redirect(request, 'home/logout.html')

def detail(request):
    pass
