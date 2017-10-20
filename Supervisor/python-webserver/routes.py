import bottle
from bottle import run, post, request, response, get, route, template, static_file



bottle.TEMPLATE_PATH.insert(0, 'app/views/')

@route('/', method = 'get')
def home_page():
	# response.set_header('Content-type', 'image/jpeg')
	return template('index.tpl', User='')
@route('/alarmpage', method = 'get')
def alarm_page():	
	return template('alarmPage.tpl', User='')


@route('/js/<filename>', method = 'get')
def js(filename):
	return static_file(filename, root='app/assets/js')
@route('/css/<filename>', method = 'get')
def css(filename):
	return static_file(filename, root='app/assets/css')
@route('/fonts/<dirName>/<filename>', method = 'get')
def fonts(dirName, filename):
	return static_file(filename, root='app/assets/fonts/' + dirName)