import pymongo
from pymongo import MongoClient
from bottle import template

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['test']
Alarm = db['Alarm']

print(Alarm.find().sort('$natural', 1).limit(1))

def getAlarms(limit=10):
	alarms = []
	for data in Alarm.find().sort('$natural', 
		pymongo.DESCENDING).limit(limit):
		alarms.append(data)
	return alarms

def createRow(alarm=None, ack='1'):
	if alarm == None:
		return False
	else:
		return template('layouts/alarm_table_row.tpl', acknowledged=ack,
			alarm_id=alarm["alarm_id"],
			event_id=alarm["event_id"],
			home_monitor_id=alarm["home_monitor_id"],
			sensor_id=alarm["sensor_id"],
			time_of_event=alarm["time_of_event"],
			description=alarm["description"],
			state=alarm["state"],
			state_history=alarm["state_history"],
			acknowledged_by=alarm["acknowledged_by"],
			acknowledged_at=alarm["acknowledged_at"])