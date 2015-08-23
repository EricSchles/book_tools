#server
from flask import Flask, render_template, request
import requests
import pickle
from mapper import Mapper
from multiprocessing import Process
import json
import time
from subprocess import call

app = Flask(__name__)

@app.route("/remove/<website>",methods=["GET","POST"])
def remove(website):
    websites = json.load(open("websites.json","r"))
    try:
        websites.remove(website)
    except ValueError:
        return "failure"
    json.dump(websites,open("websites.json","w"))
    return "success"

@app.route("/websites",methods=["GET"])
def websites():
    return pickle.dumps(json.load(open("websites.json","r")))

@app.route("/email/<address>", methods=["GET","POST"])
def email_update(address):
    emails = pickle.load(open("emails.p","rb"))
    emails.append(address)
    pickle.dump(emails,open("emails.p","wb"))
    return "success - email added"

@app.route("/phone_number/<number>", methods=["GET","POST"])
def phone_update(number):
    numbers = pickle.load(open("numbers.p","rb"))
    numbers.append(number)
    pickle.dump(numbers,open("numbers.p","wb"))
    return "success - phone number added"

@app.route("/map/<website>",methods=["GET","POST"])
def map(website):
    print website
    websites = json.load(open("websites.json","r"))
    if not website in websites:
        websites.append(website)
        json.dump(websites, open("websites.json","w"))
        tmp_website = "https://"+website
        try:
            website = requests.get(tmp_website).url
        except requests.exceptions.SSLError:
            website = requests.get("http://"+website).url
        finally:
            if not website:
                return "failure"
        m = Mapper(website)
        print "Started scraping links for "+ website
        call(["python","worker.py",pickle.dumps(m),website,str(1),pickle.dumps([])])
        
        return "success"
    return "exists"


app.run(
    debug=True,
    port=5001,
    threaded=True
)
