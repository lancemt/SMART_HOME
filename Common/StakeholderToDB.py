#before the code will execute, you must install pip and pymongo. 
#the fields and values in example below are hardcoded - during implementation, it will be replaced by method calls.
#replace NAMEOFDB, collectionname, and collectionnames with the appropriate names

from pymongo import MongoClient
client = MongoClient()
db = client.test
Stakeholder = db.Stakeholder
new_stakeholders = [{"Name": "UTS Carer",
               "Type": "Carer",
               "Phone number": "+61449827035",
               "Email": "manujayakankanige23@gmail.com"},
                    {"Name": "UTS Medical Staff",
               "Type": "Medical Staff",
               "Phone number": "+61449827035",
               "Email": "manujayakankanige23@gmail.com"},
                {"Name": "UTS Emergency",
               "Type": "Emergency Services",
               "Phone number": "+61449827035",
               "Email": "manujayakankanige23@gmail.com"}]
result = Stakeholder.insert_many(new_stakeholders)
result.inserted_ids
