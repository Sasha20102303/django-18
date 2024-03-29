from django.shortcuts import render
from .models import User
from .forms import UserLoginForm
from django.urls import reverse
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
    else:
        form = UserLoginForm()
    context = {
        'form':form,
    }
    return render(request, 'users/login.html', context=context)

def register(request):
    return render(request, 'users/register.html')



# Create your views here.
