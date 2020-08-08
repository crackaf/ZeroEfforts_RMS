from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/index.html')


def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            user = authenticate(
                username=request.POST.get("username"),
                password=request.POST.get("password"))
            if user is not None:
                # A backend authenticated the credentials
                print(user.password)
                return render(request, 'home/index.html')
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/index.html')


def logout(request):
    logout(request)
    return redirect(request, 'home/login.html')


def contact(request):
    pass


def about(request):
    pass
