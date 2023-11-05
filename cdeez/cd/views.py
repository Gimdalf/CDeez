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
		user_completed = []
		if user_data == None:
			driver.addUser(username)
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

def semester(request):
	template = loader.get_template('cd/semester.html')
	context = {
		'courses': [x["_id"] for x in driver.getCoursesWithDiscipline("CSC")]
	}
	return HttpResponse(template.render(context, request))

def major_progress(request):
	if request.user.is_authenticated:
		template = loader.get_template('cd/major.html')
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

				premajorCourses = []
				for i in major_obj['premajor']:
					if i['courses'] != None:
						premajorCourses += i['courses']
				major_obj['form'] = CompletionForm(premajorCourses)
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
		if form.is_valid():
			user = authenticate(username = form['username'].data, password = form['password'].data)
			if user is not None:
				login(request, user)
				return redirect('cd:index') # FIXME:
			else:
				pass
	return HttpResponse(template.render(context, request))

def select_major(request):
	template = loader.get_template('cd/select_major.html')
	allMajors = list(x for x in driver.getAllMajors())
	context = {
		'majors': allMajors,
		'majorForm': MajorForm([(x['_id'], x['name']) for x in allMajors])
	}
	pprint(context['majorForm'])
	if request.method == 'POST':
		if request.user.is_authenticated:
			form = MajorForm(choices = [(x['_id'], x['name']) for x in allMajors], data = request.POST)
			if form.is_valid():
				id = request.user.id
				pprint(form)
				major_input = form.data['major']
				for i in allMajors:
					if major_input.lower() == i['_id'].lower():
						driver.addMajorToUser(id, major_input.upper())
						return redirect('cd:major_progress')
			else:
				pprint(form.errors)
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



#Lucy
def major(request):
	if request.user.is_authenticated:
		template = loader.get_template('cd/major.html')
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
				for i in range(len(major_obj['premajor'])):
					pos = major_obj['premajor'][i]
					completedCoursesInSection = checkRequirement(user_completed, major_obj['premajor'][i])
					major_obj['premajor'][i]['form'] = CompletionForm(major_obj['premajor'][i]['courses'], initial = {x: True for x in completedCoursesInSection})
				updateRequirementsCompletion(user_completed, major_obj['core'])
				for i in range(len(major_obj['core'])):
					pos = major_obj['core'][i]
					completedCoursesInSection = checkRequirement(user_completed, major_obj['core'][i])
					major_obj['core'][i]['form'] = CompletionForm(major_obj['core'][i]['courses'], initial = {x: True for x in completedCoursesInSection})
				electiveList = major_data['requirements']['electives']
				major_obj['electives'] = []
				for el in electiveList:
					eReq = driver.electiveToRequirements(el)
					major_obj['electives'] += eReq
				updateRequirementsCompletion(user_completed, major_obj['electives'])
				for i in range(len(major_obj['electives'])):
					pos = major_obj['electives'][i]
					completedCoursesInSection = checkRequirement(user_completed, major_obj['electives'][i])
					major_obj['electives'][i]['form'] = CompletionForm(major_obj['electives'][i]['courses'], initial = {x: True for x in completedCoursesInSection})
				majors.append(major_obj)

		context = {
			'username': username,
			'majors': majors
		}
		return HttpResponse(template.render(context, request))
	else:
		return redirect("cd:login")


	
	context = {
		'majors':[
			{'name':'Computer Science',
			'premajor':[
				{'name':'Math',
				'completed':['MATH150'],
				'noOfRequired':2,
				'courses':['MATH150', 'MATH161']}, 
				{'name':'CS','completed':['CSC171'],
	 			'noOfRequired':3,
				'courses':['CSC171','CSC172','CSC173']}
			]
			},
			{'name':'Data Science'}
		]
	}
	template = loader.get_template('cd/major.html')
	return HttpResponse(template.render(context, request))

