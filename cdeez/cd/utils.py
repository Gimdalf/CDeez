from pymongo import MongoClient
import configparser
from pprint import pprint

class Driver:
	def __init__(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		server_settings = config['SERVER_SETTINGS']
		self.client = MongoClient(server_settings['connection_string'])
		self.mongoDB = self.client[server_settings['db_name']]
		self.coursesDB = self.mongoDB.Courses
		self.majorsDB = self.mongoDB.Majors
		self.usersDB = self.mongoDB.Users
		self.semesterDB = self.mongoDB.Semester


	def addCourse(self, id, subid, name, terms, prereqs, subject, credits):
		post = {
			"_id":id,
			"subid": subid,
			"name": name,
			"terms": terms,
			"prereqs": prereqs,
			"subject": subject,
			"credits": credits
		}
		return self.coursesDB.insert_one(post).inserted_id
	
	def getCourseByID(self, id):
		course = self.coursesDB.find_one({"_id":id})
		return course
	
	def addMajor(self, id, name, discipline, premajor, core, electives, credits):
		post = {
			"_id": id,
			"name": name,
			"discipline": discipline,
			"premajor": premajor,
			"core": core,
			"electives": electives,
			"credits": credits
		}
		return self.majorsDB.insert_one(post).inserted_id

	def getMajorByID(self, id):
		major = self.majorsDB.find_one({"_id":id})
		return major
	
	def getAllMajors(self):
		return self.majorsDB.find()

	def newRequirement(self, courses, minCompletion):
		requirement = {
			"courses": courses,
			"minCompletion": minCompletion
		}
		return requirement
	
	def createElective(self, courses, noCourses, fromDisciplines, aboveTwoHundred):
		elective = {
			"courses": courses,
			"noCourses": noCourses,
			"fromDisciplines": fromDisciplines,
			"aboveTwoHundred": aboveTwoHundred
		}
		return elective

	def addUser(self, id, username):
		post = {
			"_id": id,
			"name": username,
			"majors": [],
			"minors": [],
			"clusters": []
		}
		return self.usersDB.insert_one(post).inserted_id

	def getUserByID(self, id):
		return self.usersDB.find_one({"_id":id})

	def addMajorToUser(self, id, major):
		user = self.usersDB.find_one({'_id': id})
		oldMajors = []
		if user['majors'] != None:
			oldMajors = user['majors']
		oldMajors.append(major)
		return self.usersDB.update_one({'_id': id}, {'$set':{'majors':oldMajors}})
	
	def getAllCourses(self):
		return self.coursesDB.find()

	def getCoursesWithDiscipline(self, discipline, twoHundred = False):
		if twoHundred:
			courses = self.coursesDB.find({'_id':{"$regex": "[A-z]{3,4}2\d\d"}, 'discipline':discipline})
		else:
			courses = self.coursesDB.find('discipline: discipline')
		return courses
	
	def completeCourse(self, id, course):
		user = self.usersDB.find_one({'_id': id})
		oldCompleted = []
		if user['completedCourses'] != None:
			oldCompleted = user['completedCourses']
		oldCompleted.append(course)
		return self.usersDB.update_one({'_id': id}, {'$set':{'completedCourses':oldCompleted}})
	
	def uncompleteCourse(self, id, course):
		user = self.usersDB.find_one({'_id': id})
		return self.usersDB.update_one({'_id': id}, {'$pull':{'completedCourses':course}})
