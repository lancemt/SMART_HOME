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

def checklogin(email, psw):
    user = User.find_one({"userID": email})
    pw = base64.b64encode(hashlib.sha256(psw.encode('utf-8')).digest())
    hashed = user["password"]
    if(bcrypt.checkpw(pw, hashed)):
        al = user["accesslevel"]
        print(hashed)
        print(al)
        return al

def registerUser(email, psw, lvl):
    pw = base64.b64encode(hashlib.sha256(psw.encode()).digest())
    hashed = bcrypt.hashpw(
        pw,
        bcrypt.gensalt()
    )
    bcrypt.checkpw(pw, hashed)
    User.insert_one({
            "userID": email,
            "password": hashed,
            "accesslevel":lvl
        })
#password = b"an incredibly long password" * 10 #This was just experimentation code to check the bycrypt password
