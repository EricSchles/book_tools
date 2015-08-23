#client
from flask import Flask, render_template, request
import requests
import pickle

app = Flask(__name__)

@app.route("/keyword_add",methods=["GET","POST"])
def index():
    if request.method=="POST":
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        responses = []
        if email:
            responses.append(requests.get("http://localhost:5001/email/"+email))
        if phone_number:
            responses.append(requests.get("http://localhost:5001/phone_number/"+phone_number))
        return str([r.text for r in responses])
    return render_template("index.html")

@app.route("/forensic_mapper",methods=["GET","POST"])
def map():
    websites = pickle.loads(requests.get("http://localhost:5001/websites").text)
    if request.method=="POST":
        website = request.form.get("website")
        to_remove = request.form.get("ToRemove")
        website = website.strip("/")
        if website.startswith("http://"):
            website = website.lstrip("http://")
        elif website.startswith("https"):
            website = website.lstrip("https://")
        requests.get("http://localhost:5001/map/"+website)
        if to_remove:
            requests.get("http://localhost:5001/remove/"+to_remove)
        return render_template("mapper.html",started="started scraping " + website+ " for information",websites=websites)
    return render_template("mapper.html",websites=websites)

app.run(
    debug=True,
    threaded=True
)
