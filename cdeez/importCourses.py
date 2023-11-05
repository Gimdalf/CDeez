from cd.utils import Driver
import json

x = '''
'''

driver = Driver()

json_import = json.loads(x)
print("JSON imported")

driver.addCourses(json_import)