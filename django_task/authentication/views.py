from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import auth, messages
from django.contrib.auth import get_user_model

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request, 'You are logged in')
            return redirect('home')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'authentication/login.html') 

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'email exists, Try again')
                return redirect('signup')
            else:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'username already exists')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(email=email, username=username, address=address, password=password)
                    user.save()
                    messages.success(request, 'Account created successfully, Login to you account')
                    return redirect('login')
        else:
            messages.warning(request, 'Password do not match')
            return redirect('signup')
    
    return render(request, 'authentication/signup.html') 


def logout_user(request):
    logout(request)
    return redirect('home')