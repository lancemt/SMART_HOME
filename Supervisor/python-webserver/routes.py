import subprocess
import bottle
from bottle import run, post, request, response, get, route, template, static_file, redirect

from time import sleep
from populateAlarmTable import getAlarms, createRow

bottle.TEMPLATE_PATH.insert(0, 'app/views/')

@route('/', method = 'get')
def home_page():
	# response.set_header('Content-type', 'image/jpeg')
	return template('index.tpl', User='')
@route('/alarmpage', method = 'get')
def alarm_page():
	data = ""
	ack_data = ""
	for row in getAlarms():
		if row['acknowledged_by']:
			ack_data += createRow(row, 1)
		else:
			data += createRow(row, "")
	return template('alarmPage.tpl', User='testUserEmail@email.we', data=data, ack_data=ack_data)
@route('/login', method='post')
def login():
	username = request.forms.get('email')
	password = request.forms.get('password')
	print(username, password)
	redirect('/alarmpage')
@route('/wait', method='post')
def waiting():
	sleep(10)
	redirect('/alarmpage')

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


@route('/hello')
def hello_again():
	if request.get_cookie("visited"):
		return "Welcome back! Nice to see you again"
	else:
		response.set_cookie("visited", "yes")
		return "Hello there! Nice to meet you"