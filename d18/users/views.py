from django.shortcuts import render
from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserCreationForm
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

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
                print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'form':form,
    }
    return render(request, 'users/login.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))

        else:
            form = UserRegistrationForm()
        context = {'form': form,}
    return render(request, 'users/register.html', context=context)




@login_required
def profile(request):
        if request.method == "POST":
            form = UserProfileForm(instance=request.user, data = request.POST, files=request.FILES),
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('users:profile'))
            else:
                print(form.errors)
        else:
            form = UserProfileForm(instance=request.user)
        context = {'title': 'Профиль', 'form': form, }
        return render(request, 'users/profile.html', context=context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


