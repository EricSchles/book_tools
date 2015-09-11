
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

#http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku

class Logger(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ip_address = db.Column(db.String(400))
	timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

	def __init__(self,ip_address):
		self.ip_address = ip_address

	def __repr__(self):
		return '<ip_addr %r>' % self.ip_address


@app.route("/index")
@app.route("/")
def index():
	if request.headers.getlist("X-Forwarded-For"):
   		ip = request.headers.getlist("X-Forwarded-For")[0]
	elif request.access_route:
		ip = request.access_route
	else:
   		ip = request.remote_addr
	log = Logger(ip)
	db.session.add(log)
	db.session.commit()
	return render_template("index.html")




if __name__ == '__main__':
	app.run(debug=True)
