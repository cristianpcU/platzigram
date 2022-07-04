"""Modulo de user view"""
from cgitb import reset
from curses import erasechar
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method=='POST':
        user_name = request.POST['user']
        user_pass = request.POST['password']
        user=authenticate(request, username=user_name,password=user_pass)
        if user:
            login(request, user=user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'ERROR LOGIN'})

    return render(request,'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')