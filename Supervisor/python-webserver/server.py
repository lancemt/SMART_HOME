#!/usr/bin/env python

from bottle import run
from pymongo import MongoClient

import routes # Setup Routes


client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['test']
sensortag_data = db['users']

# ============= #
# SERVER STARTS #
# ============= #
run(host='0.0.0.0', port=3000, debug=True)
