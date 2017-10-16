#before the code will execute, you must install pip and pymongo. 
#the fields and values in example below are hardcoded - during implementation, it will be replaced by method calls.
#replace NAMEOFDB, collectionname, and collectionnames with the appropriate names

from pymongo import MongoClient
client = MongoClient()
db = client.NAMEOFDB
collectionname = db.collectionname
new_collectionnames = [{"fieldheader": "somevalue",
               "fieldheader1": "somevalue1",
               "fieldheader2": "somevalue2"},
		{"fieldheader": "somevalue",
               "fieldheader1": "somevalue1",
               "fieldheader2": "somevalue2"}]
result = collectionname.insert_many(new_collectionnames)
result.inserted_ids
