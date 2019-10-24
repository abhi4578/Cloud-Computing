from django.shortcuts import render
from .forms import PostForm
	
# Create your views here.

def home(request):
	return render(request, 'landing/index.html', {})


from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import templates
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def login1(request):
	print("Hitting Home Page Successfull111")

	#return HttpResponse("Done and dusted")
	return render(request,'landing/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')


def signup(request):
	return render(request,'landing/signup.html')


def signup_submit(request):
    print("Creating a new user")
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = User.objects.create_user(username, email,password)
    user.save()
    return redirect('/')



def logging_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request,user)
        return redirect('/')
        # Redirect to a success page.
        ...
    else:
        return redirect('/login')
        # Return an 'invalid login' error message.
        ...	