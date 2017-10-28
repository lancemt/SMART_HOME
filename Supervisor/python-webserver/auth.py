import bcrypt
import base64
import hashlib
import pymongo
import hashlib

from datetime import datetime, timedelta
from time import time

client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
User = db['User']

def checklogin(id, str):
    user = User.find_one({"userID": id})
    pw = base64.b64encode(hashlib.sha256(str.encode('utf-8')).digest())
    hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
    print("input:")
    print(pw)
    print("Stored:")
    spw = base64.b64encode(hashlib.sha256(user["password"].encode('utf-8')).digest())
    print(spw)
    if pw == spw:
        al = user["accesslevel"]
        print(hashed)
        print(al)
        return al


#password = b"an incredibly long password" * 10 #This was just experimentation code to check the bycrypt password
#pw = base64.b64encode(hashlib.sha256(password).digest())
#hashed = bcrypt.hashpw(
#	pw,
#	bcrypt.gensalt()
#)

#bcrypt.checkpw(pw, hashed)
