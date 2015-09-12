from flask import Flask, request, redirect
import twilio.twiml
from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime
 
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
 
# Try adding your own number to this li
class Logger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caller = db.Column(db.String(400))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self,caller):
        self.caller = caller

    def __repr__(self):
        return '<ip_addr %r>' % self.ip_address

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")    
    print from_number
    if from_number:
        call = Logger(from_number)
        db.session.add(call)
        db.session.commit()
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
