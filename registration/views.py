from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import user
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        oname = request.POST['oname']
        pwd = request.POST['pwd']

        storeInTable = user(fname=fname, lname=lname,
                            email=email, oname=oname, pwd=pwd)
        storeInTable.save()
        print('User Created')
        return redirect('login')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        if user.objects.filter(email=email, pwd=pwd).exists():
            request.session['email'] = email
            return redirect('dashboard')
    else:
        return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return redirect('home')
