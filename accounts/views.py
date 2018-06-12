from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse('you password was wrong you stupid asshole')
    else:
        login_form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': login_form})

def register(request):
    registration_form = UserRegistrationForm()  #..........creates an empty form
    return render(request, 'accounts/register.html', {'form': registration_form})

def logout(request):
    # return HttpResponse('Do you want to logout')
    auth.logout(request)
    return redirect('/')
    
    