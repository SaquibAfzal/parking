from telnetlib import AUTHENTICATION
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'index.html')
    # Do something for anonymous users.
def search(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'search.html')
def display(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/login')
        # Do something for authenticated users.
    return render(request, 'display.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')
