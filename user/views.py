from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username,email=email, password=password)
        
        
    
    return render(request, 'register.html')
