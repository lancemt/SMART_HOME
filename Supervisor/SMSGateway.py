from twilio.rest import Client

# Twilio Account SID, Auth Token and Number
sid = "AC67007313a1dafe04cdf31150431ec96e"
auth = "cc4afdbb9052992396e228ed60caa253"
sender = "+17738394331"

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
