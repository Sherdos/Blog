from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email, password=password)
        login(request,user)
        return redirect('home')
    return render(request, 'register.html')

def user_login(request):
    return render(request, 'login.html')