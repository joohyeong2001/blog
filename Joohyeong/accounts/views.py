from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')
        

def signup(request):
    if request.method =="POST":
        if request.POST['password'] == request.POST['re-enter password']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('index')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('index')