from django.shortcuts import render
from .models import User
from .forms import UserLoginForm
from django.auth import reverse


def login(request):
    context = {
        'form':UserLoginForm(),
    }
    return render(request, 'users/login.html', context=context)

def register(request):
    return render(request, 'users/register.html')



# Create your views here.
