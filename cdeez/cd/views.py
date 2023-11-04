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
	template = loader.get_template('cd/index.html')
	username = None
	major = None
	if request.user.is_authenticated:
		username = request.user.get_username()
		user_data = driver.getUserByID(request.user.id)
		majors = user_data['majors']
		print(request.user.id)
	context = {
		'username': username,
		'majors': majors
	}

	return HttpResponse(template.render(context, request))

def viewCourse(request, course = None):
	courseData = driver.getCourse(course)
	return HttpResponse("ID:{}\n {}\n {}".format(courseData["_id"], courseData["title"], courseData["term"]))

def majorProgress(request):
	if request.user.is_authenticated:
		username = request.user.get_username()
		user_data = driver.getUserByID(request.user.id)
		majors = []
		majors_from_db = user_data['majors']
		for major in majors_from_db:
			major_obj = {}
			major_data = driver.getMajorByID(major)
			if major_data == None:
				continue
			else:
				major_obj['name'] = major_data['name']
				# Getting premajor requirements
				major_obj['premajor'] = major_data['requirements']['premajor']
				major_obj['core'] = major_data['requirements']['core']
				electiveList = major_data['requirements']['electives']
				major_obj['electives'] = []
				for el in electiveList:
					elective_obj = {'name': el['name'], 'courses': []}
					noOfCourses = el['noCourses']
					if el['courseList'] == None or el['courseList'] == []:
						#If there are no specified disciplines
						if el['fromDisciplines'] == None or el['fromDisciplines'] == []:
							allCourses = driver.getAllCourses()
							elective_obj['courses'] = [allCourses for i in noOfCourses]
						#If disciplines are specified
						else:
							disciplineCourses = driver.getCoursesWithDiscipline(d)
							twoHundredCourses = []
							noTwoHundredCourses = el['aboveTwoHundred']
							if noTwoHundredCourses > 0:
								twoHundredCourses = [driver.getCoursesWithDiscipline(d, True) for d in el['fromDisciplines']]
							elective_obj['courses'] = [disciplineCourses for i in range(noOfCourses - noTwoHundredCourses)] + [twoHundredCourses for i in range(noTwoHundredCourses)]
					else:
						elective_obj['courses'] = [el['courseList'] * noOfCourses]
					major_obj['electives'].append(elective_obj)
				majors.append(major_obj)

		context = {
			'username': username,
			'majors': majors
		}
	else:
		return HttpResponse("Not logged in: nothing to see here")

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

def select_major(request):
	template = loader.get_template('cd/select_major.html')
	context = {
		'majorForm': MajorForm()
	}
	if request.method == 'POST':
		if request.user.is_authenticated:
			id = request.user.id
			form = MajorForm(request.POST)
			if form.is_valid:
				majors = driver.getAllMajors()
				major_input = form['major'].data
				for i in majors:
					if major_input.lower() == i['_id'].lower():
						driver.addMajorToUser(id, major_input.upper())
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
				driver.addUser(user.id, user.username)
				login(request, user)
				return redirect('cd:index')
			else:
				pass
	return HttpResponse(template.render(context, request))

def logout_user(request):
	logout(request)
	return redirect('cd:index')