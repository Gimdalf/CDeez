from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

from .utils import Driver

driver = Driver()

def index(request):
	return HttpResponse("Hello CDeez User")

def viewCourse(request, course = None):
	courseData = driver.getCourse(course)
	return HttpResponse("ID:{}\n {}\n {}".format(courseData["_id"], courseData["title"], courseData["term"]))