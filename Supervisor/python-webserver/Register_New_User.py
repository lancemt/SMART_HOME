import bcrypt
import base64
import hashlib
import pymongo
import hashlib

client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
User = db['User']

def test():
        registerUser("Doctor@smarthome.com","doctor","0")



def registerUser(email, psw, lvl):
    pw = base64.b64encode(hashlib.sha256(psw).digest())
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
