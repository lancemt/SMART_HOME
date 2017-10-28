import uuid
import pymongo
import datetime
from time import sleep

def populate():
	try:
		populate.id
	except:
		populate.id = 1000
	populate.id += 1
	test = {
		"alarm_id": str(uuid.uuid4()),
		"event_id": populate.id,
		"home_monitor_id": "HM1",
		"sensor_id": "AGJJ74",
		"time_of_event": datetime.datetime.today(),
		"description": "Some Description2",
		"state": "Urgent",
		"state_history": "",
		"acknowledged_by": "",
		"acknowledged_at": ""
	}
	return test

client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
Alarm = db['Alarm']

for i in range(10):
	sleep(0.1)
	Alarm.insert_one(populate())
