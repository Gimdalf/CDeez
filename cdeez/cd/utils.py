import math
from pymongo import MongoClient
import configparser
from pprint import pprint

# requirements must have: "noOfRequired":int, "courses":
def checkRequirement(completedCourses, requirement):
	noRequired = requirement['noOfRequired']
	completed = []
	for i in requirement['courses']:
		pprint(requirement['courses'])
		if i in completedCourses:
			completed.append(i)
		if len(completed) >= noRequired:
			return completed
	return []

def updateRequirementsCompletion(completedCourses, requirements):
	for i, data in zip(range(len(requirements)), requirements):
		completingCourses = checkRequirement(completedCourses, data)
		requirements[i]['completed'] = completingCourses

# currenty just getting progress for first major
# requirements refers to a collection of requirements. Returns tuple (no. of completed courses, no. of total courses)
def requirementProgress(completedCourses, requirements):
	totalCourses = 0
	totalComplete = 0
	for r in requirements:
		completed = len(checkRequirement(completedCourses, r))
		totalCourses += r['noOfRequired']
		totalComplete += completed
	return (totalComplete, totalCourses)

def decimalToPercentage(x):
	return math.ceil(x*100)

def percentifyValues(x):
	if x[1] != 0:
		return math.ceil((x[0]/x[1])*100)
	else:
		return 100

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
		self.clustersDB = self.mongoDB.Clusters
		# self.semesterDB = self.mongoDB.Semester


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
	
	def addCourses(self, courses):
		return self.coursesDB.insert_many(courses)

	def getCourseByID(self, id):
		course = self.coursesDB.find_one({"_id":id})
		return course
	
	def getAllCourses(self):
		return self.coursesDB.find()

	def getCoursesWithDiscipline(self, discipline, twoHundred = False):
		if twoHundred:
			courses = self.coursesDB.find({'_id':{"$regex": "[A-z]{3,4} 2\d\d"}, 'discipline':discipline})
		else:
			courses = self.coursesDB.find({'discipline': discipline})
		return courses
	
	def getAllULWCourses(self):
		return self.courseDB.find("")

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
			"completedCourses": [],
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
	
	def electiveToRequirements(self, el):
		newReqCollection = []
		elective_obj = {'name': el['electiveName'], 'courses': [], 'noOfRequired': el['noCourses']}
		noOfCourses = el['noCourses']

		if el['courseList'] == None or el['courseList'] == []:
			#If there are no specified disciplines
			if el['fromDisciplines'] == None or el['fromDisciplines'] == []:
				allCourses = self.getAllCourses()
				elective_obj['courses'] = [list(j for j in allCourses) for i in noOfCourses]
			#If disciplines are specified
			else:
				disciplineCourses = []
				twoHundredCourses = []
				noTwoHundredCourses = el['aboveTwoHundred']
				for d in el['fromDisciplines']:
					disciplineCourses.append(i for i in self.getCoursesWithDiscipline(d))
					if noTwoHundredCourses > 0:
						twoHundredCourses += [i for i in self.getCoursesWithDiscipline(d, True) for d in el['fromDisciplines']]
				if noTwoHundredCourses > 0:
					otherElectiveObj = elective_obj.copy()
					otherElectiveObj['courses'] = twoHundredCourses
					otherElectiveObj['noOfRequired'] = noTwoHundredCourses
					newReqCollection.append(otherElectiveObj)

				elective_obj['courses'] = disciplineCourses
				elective_obj['noOfRequired'] = noOfCourses - noTwoHundredCourses

		else:
			elective_obj['courses'] = [el['courseList'] * noOfCourses]
		newReqCollection.append(elective_obj)

		return newReqCollection
	
	def createCluster(self, name, discipline, requirements):
		post = {
			"_id": name,
			"discipline": discipline,
			"requirements": requirements
		}
		return self.clustersDB.insert(post)
	
	def getClusterByName(self, name):
		return self.clustersDB.find_one({"_id": name})
	
	def getAllClusters(self):
		return self.clustersDB.find()