import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

class Emailer:
    
    def __init__(self,addr='',pw="",website=None):
        self.addr = addr
        self.pw = pw
        self.msg = MIMEMultipart('alternative')
        self.receiver = ['']
        if website:
            self.msg['Subject'] = "Update to website"+website
        else:
            self.msg['Subject'] = "Update to website"
        self.msg["From"]=self.addr
        self.msg["To"] = ','.join(self.receiver)
        
    def add_message(self,text):
        if type(text) == type(' '):
            tmp = MIMEText(text,'plain')
            self.msg.attach(tmp)
    def send(self):
        s = smtplib.SMTP('smtp.gmail.com', 587) #used because I don't know how to use Outlook SMTP
        s.starttls()
        s.login(self.addr, self.pw)
        s.sendmail(self.addr, self.receiver, self.msg.as_string()) 
        s.close()
    def add_website(self,site):
        self.website = website
        self.msg['Subject'] = "Update to website"+website

    
