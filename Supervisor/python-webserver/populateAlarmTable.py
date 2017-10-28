import pymongo
from bottle import template
import datetime

client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
Alarm = db['Alarm']

def updateAlarmById(id, state):
	alarm = Alarm.find_one({"alarm_id": id})
	alarm = Alarm.find_one_and_update({"alarm_id": id},
		{'$set':
		{
			"acknowledged_by":"TODO:fixme",
			"acknowledged_at":datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
			"state":state,
			"state_history":(
				(alarm['state'] if alarm['state'] != state else ''))  +
				(', ' if (alarm['state_history'] and alarm['state'] != state) else '') +
				alarm['state_history']
		}}, return_document=pymongo.ReturnDocument.AFTER)
	return createRow(alarm, ack=1)

def getAlarms(limit=0):
	alarms = []
	for data in Alarm.find().sort('time_of_event:',pymongo.ASCENDING).limit(limit):
		alarms.append(data)
	return alarms

def refAlarms(latestDate):
	alarms = []
	for doc in Alarm.find().sort('time_of_event', pymongo.DESCENDING):
		if(latestDate != None and
			float(latestDate) >= doc['time_of_event'].timestamp()
			):
			# alarms.reverse()
			return alarms[::-1]
		alarms.append(doc)
	# alarms.reverse()
	return alarms[::-1]

def createRow(alarm=None, ack='1'):
	if alarm == None:
		return False
	else:
		return template('layouts/alarm_table_row.tpl', acknowledged=ack,
			alarm_id=alarm["alarm_id"],
			event_id=alarm["event_id"],
			home_monitor_id=alarm["home_monitor_id"],
			sensor_id=alarm["sensor_id"],
			time_of_event=#alarm["time_of_event"].strftime("%Y-%m-%d %H:%M:%S.%f"),
			'{d.year}-{d.month:02d}-{d.day:02d} {d.hour:02d}:{d.minute:02}:{d.second:02}.{m}'.format(d=alarm["time_of_event"], m=str(alarm["time_of_event"].microsecond)[:3]),
			description=alarm["description"],
			state=alarm["state"],
			state_history=alarm["state_history"],
			acknowledged_by=alarm["acknowledged_by"],
			acknowledged_at=alarm["acknowledged_at"])