#!/usr/bin/env python

import threading
from gevent import monkey; monkey.patch_all()
from bottle import run

import routes # Setup Routes

# ============= #
# SERVER STARTS #
# ============= #
# run(host='0.0.0.0', port=3000, debug=True)
threading.Thread(target=run, kwargs=dict(host='0.0.0.0', port=3000, server='gevent', debug=False)).start()
