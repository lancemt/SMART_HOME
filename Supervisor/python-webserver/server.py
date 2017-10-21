#!/usr/bin/env python

import threading
from gevent import monkey; monkey.patch_all()
import bottle
from bottle.ext import beaker

import routes # Setup Routes


session_opts = {
	'session.cookie_expires': True,
	'session.encrypt_key': 'please use a random key and keep it secret!',
	'session.httponly': True,
	'session.timeout': 60*5,#3600 * 24,  # 1 day
	'session.type': 'cookie',
	'session.validate_key': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

# ============= #
# SERVER STARTS #
# ============= #
# run(host='0.0.0.0', port=3000, debug=True)
threading.Thread(target=bottle.run, kwargs=dict(app=app, host='0.0.0.0', port=3000, server='gevent', debug=False)).start()
