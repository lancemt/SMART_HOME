import pymongo
import datetime

from SMSGateway import SMS
from EmailGateway import Email

client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
db = client['test']
Stakeholder = db['Stakeholder']

def createReport(state, description):
    if state == "Non-Critical":
        stakeholder = Stakeholder.find_one({"Type": "Carer"})
        phonenumber = stakeholder["Phone number"]
        emailaddress = stakeholder["Email"]
        SMS(phonenumber, state, description) 
        Email(emailaddress, state, description)
        
    elif state == "Urgent":

        stakeholder = Stakeholder.find_one({"Type": "Medical Staff"})
        phonenumber = stakeholder["Phone number"]
        emailaddress = stakeholder["Email"]
        SMS(phonenumber, state, description) 
        Email(emailaddress, state, description)
        
    elif state == "Critical":

        stakeholder = Stakeholder.find_one({"Type": "Emergency Services"})
        phonenumber = stakeholder["Phone number"]
        emailaddress = stakeholder["Email"]
        SMS(phonenumber, state, description) 
        Email(emailaddress, state, description)
        
    else:
        pass
        
