from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from User.forms import UserRegistrationForm
from django.db.models import Q


def home(request):
	return render(request,'User/home.html')#returns the home page

def register(request):
	if request.method =='POST':
		form = UserRegistrationForm(request.POST)#posts user info
		if form.is_valid():
			user = form.save()#saves user 
			#username = form.cleaned_data.get('username')
			login(request,user)
			messages.success(request, f'Account created for {{user}}!')#alter message shown
			return redirect('home')
	else:
		form = UserRegistrationForm()
	return render(request, 'User/register.html', {'form': form})

def user_logout(request):
	logout(request)
	return redirect('home')

def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")

			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.success(request, f'You have logged as {{ username }}')
				return redirect('home')

	form = AuthenticationForm()
	return render(request, 'User/login.html',
		{"form":form})

def profile(request):
	return render(request,'User/profile.html')
