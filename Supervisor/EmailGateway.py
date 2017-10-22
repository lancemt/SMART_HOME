import smtplib

# Preset sender infromation
sender_email = "smarthomebronte@gmail.com"
sender_pw = "smarthome2017"

class Email:
    def __init__(self, receiver, state, message):
        self.des = receiver
        self.msg = 'Subject: %s\n%s' % (state + " Alarm", message)
        self.send()
        
    def send(self):
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email,sender_pw)
        mail.sendmail(sender_email, self.des ,self.msg)
        mail.close()
        print("Email sent!")

