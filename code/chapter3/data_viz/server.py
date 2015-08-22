from flask import Flask,render_template
import json
from random import randint
app = Flask(__name__)

@app.route("/line_chart",methods=["GET","POST"])
def line_chart():
    data1 = ['data1']
    data2 = ['data2']
    for i in xrange(0,randint(0,15)):
        data1.append(randint(0,150))
    for i in xrange(0,randint(2,25)):
        data2.append(randint(7,450))
    return render_template("line_chart.html",data1=json.dumps(data1),data2=json.dumps(data2),data3=json.dumps(data1))

@app.route("/spline_chart",methods=["GET","POST"])
def spline_chart():
    data1 = ['data1']
    data2 = ['data2']
    for i in xrange(0,randint(0,15)):
        data1.append(randint(0,150))
    for i in xrange(0,randint(2,25)):
        data2.append(randint(7,450))
    return render_template("spline_chart.html",data1=json.dumps(data1),data2=json.dumps(data2),data3=json.dumps(data1))

@app.route("/bar_chart",methods=["GET","POST"])
def bar_chart():
    data1 = ['data1']
    data2 = ['data2']
    for i in xrange(0,randint(0,15)):
        data1.append(randint(0,150))
    for i in xrange(0,randint(2,25)):
        data2.append(randint(7,450))
    return render_template("bar_chart.html",data1=json.dumps(data1),data2=json.dumps(data2),data3=json.dumps(data1))

@app.route("/pie_chart",methods=["GET","POST"])
def pie_chart():
    data1 = ['data1']
    data2 = ['data2']
    for i in xrange(0,randint(0,15)):
        data1.append(randint(0,150))
    for i in xrange(0,randint(2,25)):
        data2.append(randint(7,450))
    return render_template("pie_chart.html",data1=json.dumps(data1),data2=json.dumps(data2),data3=json.dumps(data1))



app.run(debug=True)

