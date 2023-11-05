from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

from .utils import *
from .forms import *

driver = Driver()

def index(request):
	if request.user.is_authenticated:
		template = loader.get_template('cd/index.html')
		username = request.user.get_username()
		user_data = driver.getUserByID(request.user.id)
		user_completed = set(i for i in user_data['completedCourses'])
		majors = []
		if not 'majors' in user_data:
			return redirect("cd:select_major")
		majorsCompletion = [0, 0]
		for m in user_data['majors']:
			major = driver.getMajorByID(m)
			premajorCompletion = requirementProgress(user_completed, major['requirements']['premajor'])
			coreCompletion = requirementProgress(user_completed, major['requirements']['core'])
			electiveCompletion = [0, 0]
			for el in major['requirements']['electives']:
				asReq = driver.electiveToRequirements(el)
				reqProg = requirementProgress(user_completed, asReq)
				electiveCompletion[0] += reqProg[0]
				electiveCompletion[1] += reqProg[1]
			totalCompletion = (premajorCompletion[0] + coreCompletion[0] + electiveCompletion[0], premajorCompletion[1] + coreCompletion[1] + electiveCompletion[1])
			majorsCompletion[0] += totalCompletion[0]
			majorsCompletion[1] += totalCompletion[1]
			major_obj = {
				'name': major['name'],
				'majorProgress': percentifyValues(totalCompletion),
				'premajorProgress': percentifyValues(premajorCompletion),
				'coreProgress': percentifyValues(coreCompletion),
				'electivesProgress': percentifyValues(electiveCompletion)
			}
			majors.append(major_obj)
		
		clusters = {'clusters': []}
		clustersCompletion = [0, 0]
		for cluster in user_data['clusters']:
			clusterObj = {'name': cluster['name'], 'discipline': cluster['discipline']}
			clusterCompletion = requirementProgress(user_completed, cluster['requirements'])
			clustersCompletion[0] += clustersCompletion[0]
			clustersCompletion[1] += clustersCompletion[1]
			clusterObj['cProgress'] = percentifyValues(clusterCompletion)
			clusters['clusters'].append(clusterObj)
		clusters['clustersProgress'] = percentifyValues(clustersCompletion)

		writing = {"writing105": "WRTG 105" in user_completed}
		ulwNoReq = 1 + len(majors)
		ulwFound = []
		for course in user_completed:
			pprint(course)
			if course[-1] == "W":
				ulwFound.append(course)
			if len(ulwFound) == ulwNoReq:
				break

		while len(ulwFound) < ulwNoReq:
			ulwFound.append("")
		writing['ulw'] = ulwFound
		writingCompletion = (len(ulwFound) + ("WRTG 105" in user_completed), 1 + ulwNoReq)
		writing['writingProgress'] = percentifyValues(writingCompletion)

		completeCompletion = (majorsCompletion[0] + clustersCompletion[0] + writingCompletion[0], (majorsCompletion[1] + clustersCompletion[1] + writingCompletion[1]))

		context = {
			'majors': majors,
			'clusters': clusters,
			'writing': writing,
			'progressBar': percentifyValues(completeCompletion)
		}
			
		return HttpResponse(template.render(context, request))
	else:
		return redirect("cd:login")

def view_course(request, course = None):
	courseData = driver.getCourseByID(course)
	return HttpResponse("ID:{}\n {}\n {}".format(courseData["_id"], courseData["title"], courseData["term"]))


def major_progress(request):
	if request.user.is_authenticated:
		template = loader.get_template('cd/major_progress.html')
		username = request.user.get_username()
		user_data = driver.getUserByID(request.user.id)
		user_completed = set(i for i in user_data['completedCourses'])

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
				updateRequirementsCompletion(user_completed, major_obj['premajor'])
				updateRequirementsCompletion(user_completed, major_obj['core'])
				electiveList = major_data['requirements']['electives']
				major_obj['electives'] = []
				for el in electiveList:
					eReq = driver.electiveToRequirements(el)
					major_obj['electives'] += eReq
				updateRequirementsCompletion(user_completed, major_obj['electives'])
				majors.append(major_obj)

		context = {
			'username': username,
			'majors': majors
		}
		return HttpResponse(template.render(context, request))
	else:
		return redirect("cd:login")

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
				return redirect('/home') # FIXME:
			else:
				pass
	return HttpResponse(template.render(context, request))

def select_major(request):
	template = loader.get_template('cd/select_major.html')
	context = {
		'majors': driver.getAllMajors(),
		'majorForm': MajorForm()
	}
	if request.method == 'POST':
		if request.user.is_authenticated:
			id = request.user.id
			majors = driver.getAllMajors()
			major_input = request.POST.get('major')
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


def major(request):
	context = {}
	template = loader.get_template('cd/major.html')
	return HttpResponse(template.render(context, request))












# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import user_passes_test

# from .utils import Driver
# from .forms import *

# driver = Driver()

# def index(request):
# 	username = None
# 	if request.user.is_authenticated:
# 		username = request.user.get_username()
# 		print(request.user.id)
# 	context = {
# 		'username': username
# 	}
# 	return HttpResponse("Hello User: {}".format(username))

# def viewCourse(request, course = None):
# 	courseData = driver.getCourse(course)
# 	return HttpResponse("ID:{}\n {}\n {}".format(courseData["_id"], courseData["title"], courseData["term"]))

# def login_user(request):
# 	template = loader.get_template('cd/login.html')
# 	context = {
# 		'username': request.user.get_username if request.user.is_authenticated else None,
# 		'loginForm': LoginForm()
# 	}
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid:
# 			user = authenticate(username = form['username'].data, password = form['password'].data)
# 			if user is not None:
# 				login(request, user)
# 				return redirect('cd:index')
# 			else:
# 				pass

# 	context = 
# 	return HttpResponse(template.render(context, request))

# def create_user(request):
# 	template = loader.get_template('cd/create_user.html')
# 	context = {
# 		'username': request.user.get_username if request.user.is_authenticated else None,
# 		'createUserForm': CreateUser()
# 	}
# 	if request.method == 'POST': # if user is trying to post info from the form to the page (instead of usual GET)
# 		form = CreateUser(request.POST)
# 		if form.is_valid():
# 			cdata = form.cleaned_data
# 			if cdata['password'] == cdata['password_verify']:
# 				user = User.objects.create_user(cdata['username'], cdata['email'], cdata['password'])
# 				login(request, user)
# 				return redirect('cd:index') # if press submit, and password fields match, then redirect them to user home page for THAT user
# 				# return HttpResponse(template.render(user, request))
# 			else:
# 				pass

# 	return HttpResponse(template.render(context, request)) 

# def logout_user(request):
# 	logout(request)
# 	return redirect('cd:index')


# def major(request):
# 	return render(request, "main/major.html", {})