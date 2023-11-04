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

	def addCourse(self, id, title, term, prerequisites):
		post = {
			"_id":id,
			"title":title,
			"term":term
		}
		post_id = self.coursesDB.insert_one(post).inserted_id
	
	def getCourse(self, id):
		course = self.coursesDB.find_one({"_id":id})
		return course