from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


#@login_required
def index(request):
    if request.user.is_anonymous:
        return render(request, 'account/login.html')
    else:
        return render(request, 'account/index.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')


def loginUser(request):
    if request.user.is_authenticated:
        return HttpResponse('authenticaled')

    elif request.method == 'POST':
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"))

        if user is not None:
            login(request, user)
            return redirect('.')

    return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'account/login.html')

def detail(request):
    pass
