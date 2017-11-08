import subprocess
import bottle
import pymongo
from bottle import run, post, request, response, get, route, template, static_file, redirect
from bottle.ext import beaker
from auth import checklogin
from reportcreation import createReport

from time import sleep
from populateAlarmTable import getAlarms, createRow, updateAlarmById, refAlarms

client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
Alarm = db['Alarm']

bottle.TEMPLATE_PATH.insert(0, 'app/views/')

@route('/ackConfirm', method='post')
def ackConfirm():
	id = request.forms.get('id')
	state = request.forms.get('state')
	print(state)
	return updateAlarmById(id, state)

@route('/generateReport', method='post')
def generateReport():	
	id = request.forms.get('id')
	#state = request.forms.get('state')
	alarm = Alarm.find_one({"alarm_id": id})
	state = alarm["state"]
	home_monitor_id = alarm["home_monitor_id"]
	acknowledged_at = alarm["acknowledged_at"]
	message = "An alarm with " + state  + " state was recorded at home monitor " + home_monitor_id +  ". It was acknowledged at " + acknowledged_at + ". Have a great day!"
	messageStr = str(message)
	#print(messageStr)
	stateStr = str(state)
	createReport(stateStr, messageStr)
	updateDescription(id, messageStr)

def updateDescription(id, messageStr):	
	#updateDB with message
	alarm = Alarm.find_one_and_update({"alarm_id": id},
		{'$set':
		{
			"description":messageStr,
			
		}}, return_document=pymongo.ReturnDocument.AFTER)

@route('/test')
def test():
    s = bottle.request.environ.get('beaker.session')
    s['test'] = s.get('test',0) + 1
    s['bob'] = s.get('bob',0) +2
    s.save()
    return 'Test counter: %d, %d' % (s['test'], s['bob'])

@route('/', method = 'get')
def home_page():
	return template('index.tpl', User='')

@route('/alarmpage', method = 'get')
def alarm_page():
        #s = bottle.request.environ.get('beaker.session')
        data = ""
        ack_data = ""
        row = None
        for row in getAlarms():
                if row['acknowledged_by']:
                        ack_data += createRow(row, 1)
                else:
                        data += createRow(row, "")
	#s['latestDate'] = row['time_of_event'] if row != None else None
	#s.save()
        return template('alarmPage.tpl', User='testUserEmail@email.we', data=data, ack_data=ack_data)

@route('/login', method='post')
def login():
	username = request.forms.get('email')
	password = request.forms.get('password')
	print(username, password)
	acslvl = checklogin(username, password)
	#Check Login details here and if it works then run redirect, otherwise, return error messa
	if int(acslvl)==0:
                print("something")
                redirect('/alarmpage')
	else:
               return "Incorrect Login Details. Please go back and Re-enter the details"
	
# Assets
@route('/js/<filename>', method = 'get')
def js(filename):
	return static_file(filename, root='app/assets/js')
@route('/css/<filename>', method = 'get')
def css(filename):
	return static_file(filename, root='app/assets/css')
@route('/fonts/<dirName>/<filename>', method = 'get')
def fonts(dirName, filename):
	return static_file(filename, root='app/assets/fonts/' + dirName)

@route('/refreshTables', method = 'post')
def refresh_tables():
	s = bottle.request.environ.get('beaker.session')
	s['latestDate'] = s.get('latestDate', None)
	s['latestId'] = s.get('latestId')
	latestDate = s['latestDate']
	latestId= s['latestId']
	print(latestDate)
	# latestDate = request.get_cookie("latestDate")
	result = []
	timeout = 0
	while(result == []):
		result = refAlarms(latestDate=latestDate, latestId=latestId)
		sleep(0.5)
		timeout += 0.5
		if(timeout >= 5):
			response.status = 299
			return "timeout"
	s['latestDate'] = result[-1]['time_of_event']
	s['latestId'] = result[-1]['_id']
	s.save()
	# response.set_cookie("latestDate", latestDate)
	data = ""
	for row in result:
		data += createRow(row, "") # HTML table rows to append
	return data


@route('/hello')
def hello_again():
	if request.get_cookie("visited"):
		return "Welcome back! Nice to see you again"
	else:
		response.set_cookie("visited", "yes")
		return "Hello there! Nice to meet you"
