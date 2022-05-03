from msilib.schema import ListView
from django.http import request
from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, UserLoginForm, SignupForm
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.template import RequestContext

from .models import account
# Create your views here.
class HomeView(TemplateView):
    template_name= 'home.html'

def signup_request(request):
	if request.method == 'GET':
		form  = SignupForm()
		context = {'form': form}
		return render(request, 'signup.html', context)
	if request.method == 'POST':
		form  = SignupForm(request.POST)
		if form.is_valid():
			# form.save()
			user = form.cleaned_data.get('firstname')
			print("User "+user)
			
			return redirect('login')
		else:
			print('Form is not valid')
			messages.error(request, 'Error Processing Your Request')
			context = {'form': form}
			return render(request, 'signup.html', context)

	return render(request, 'signup.html', {})

def register_request(request):
	if request.method == 'GET':
		form  = NewUserForm()
		context = {'form': form}
		return render(request, 'signup.html', context)
	if request.method == 'POST':
		form  = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('lastname')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')
		else:
			print('Form is not valid')
			messages.error(request, 'Error Processing Your Request')
			context = {'form': form}
			return render(request, 'signup.html', context)

	return render(request, 'signup.html', {})

def login_request(request):
	if request.method == "POST":
		# AuthenticationForm=
		# form = AuthenticationForm(request, data=request.POST)
		form = UserLoginForm(request, data= request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			# username=  form.cleaned_data.get('email')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print(f"You are now logged in as {username}.")
				return render(request=request, template_name="bloghomepage.html", context={})
			else:
				messages.error(request,"Invalid username or password.")
				print('invalid username or password')
		else:
			print('Invalid username or pass')
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")
