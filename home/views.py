from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout

# Create your views here.
def login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            user = authenticate(
                username=request.POST.get("username"),
                password=request.POST.get("password"))
        if user is not None:
            # A backend authenticated the credentials
            return HttpResponse("You are loged in")
        else:
            # No backend authenticated the credentials
            return render(request, 'home/login.html')
    else:
        return HttpResponse("You are already loged in")

        
def logout(request):
    logout(request)
    return redirect('home/login.html')
