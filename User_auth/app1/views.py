from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/')

def loginView(request):
    if request.method == 'POST':
        u = authenticate(username=request.POST['login'], password=request.POST['parol'])
        if u is None:
            return redirect('/')
        else:
            login(request, u)
            return redirect('/home/')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['login'],
            password = request.POST['parol']
        )
        return redirect('/')
    return render(request, 'reg.html')

def logoutView(request):
    logout(request)
    return redirect('/')