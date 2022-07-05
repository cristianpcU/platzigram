"""Modulo de user view"""

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.
def login_view(request):
    """ User Login
    """
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
    """User Logout"""
    logout(request)
    return redirect('login')

def signup_view(request):
    """
      Vista para registrar el usuario
     import pdb;pdb.set_trace()
    """
    if request.method=="POST":
        username=request.POST["username"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST["password"]
        passconfirm=request.POST["confirm"]
        #print(username,firstname,lastname,email,password,passconfirm)
        if password==passconfirm:
            try:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                profile= Profile(user=user)
                profile.save()     
            except IntegrityError:
                return render(request,'users/signup.html',{'error':'El usuario ya existe'})

            return redirect('login')
        else:
            return render(request,'users/signup.html',{'error':'El password no coincide'})     
    return render(request,'users/signup.html')
    
