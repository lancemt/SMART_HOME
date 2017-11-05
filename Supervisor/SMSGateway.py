from twilio.rest import Client

# Twilio Account SID, Auth Token and Number
sid = "Add SID here"
auth = "Add authentication token here"
sender = "Add twilio number here"

class SMS:
    def __init__(self, receiver, state, message):
        self.des = receiver
        self.msg = state + " Alarm\n\n" + message
        self.send()
        
    def send(self):
        client = Client(sid, auth)
        client.messages.create(to = self.des, from_= sender, body = self.msg)
        print("SMS sent!")
