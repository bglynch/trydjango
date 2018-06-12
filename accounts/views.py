from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth import logout
from django.contrib import auth

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    # return HttpResponse('Do you want to logout')
    auth.logout(request)
    return redirect('/')