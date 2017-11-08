from twilio.rest import Client

# Twilio Account SID, Auth Token and Number
sid = "ACf58c77037347f3621c6cb8dc5878f30f"
auth = "cf148e1859c3cc4b1bfdea0c5d021453"
sender = "+18312788325" 

class SMS:
    def __init__(self, receiver, state, message):
        self.des = receiver
        self.msg = state + " Alarm\n\n" + message
        self.send()
        
    def send(self):
        client = Client(sid, auth)
        client.messages.create(to = self.des, from_= sender, 
                       body = self.msg)
        print("SMS sent!")
