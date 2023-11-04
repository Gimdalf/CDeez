from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

from .utils import Driver
from .forms import *

driver = Driver()

def index(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
		print(request.user.id)
	context = {
		'username': username
	}
	return HttpResponse("Hello User: {}".format(username))

def viewCourse(request, course = None):
	courseData = driver.getCourse(course)
	return HttpResponse("ID:{}\n {}\n {}".format(courseData["_id"], courseData["title"], courseData["term"]))

def login_user(request):
	template = loader.get_template('cd/login.html')
	context = {
		'username': request.user.get_username if request.user.is_authenticated else None,
		'loginForm': LoginForm()
	}
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid:
			user = authenticate(username = form['username'].data, password = form['password'].data)
			if user is not None:
				login(request, user)
				return redirect('cd:index')
			else:
				pass
	return HttpResponse(template.render(context, request))

def create_user(request):
	template = loader.get_template('cd/create_user.html')
	context = {
		'username': request.user.get_username if request.user.is_authenticated else None,
		'createUserForm': CreateUser()
	}
	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			cdata = form.cleaned_data
			if cdata['password'] == cdata['password_verify']:
				user = User.objects.create_user(cdata['username'], cdata['email'], cdata['password'])
				login(request, user)
				return redirect('cd:index')
			else:
				pass
	return HttpResponse(template.render(context, request))

def logout_user(request):
	logout(request)
	return redirect('cd:index')