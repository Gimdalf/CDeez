from pymongo import MongoClient
import configparser

class Driver:
	def __init__(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		server_settings = config['SERVER_SETTINGS']
		self.client = MongoClient(server_settings['connection_string'])
		self.mongoDB = self.client[server_settings['db_name']]
		self.coursesDB = self.mongoDB.Courses
		self.majorsDB = self.mongoDB.Majors
		self.requirementsDB = self.mongoDB.Requirements

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

	def newRequirement(self, courses, minCompletion):
		post = {
			"courses": courses,
			"minCompletion": minCompletion
		}
		return post