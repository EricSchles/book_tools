##Chapter 3 - Data Visualization

So far we've seen how to process data and make use of statistics/machine learning to automate analysis and get stuff done.  Unfortunately for most non-technical folks working in government and non-profit land, this is really not useful.  There are a few reasons behind this:

1. You're going to leave - The government and/or non-profit don't pay very well and eventually you'll need to actually make a living, paying down student debt, raising a family, covering medical expenses, going to the dentist and a whole other laundry list of things you won't be able to afford.  Everyone knows you are leaving, because you won't be the first technologist who's ever tried to make a difference and you won't be the last.  But sadly, they really can't afford you and never will be able to.  

2. They don't actually understand what you've built - very, very few non-profits or government folks understand or embrace technology.  Which is the reason you can have such a large impact.  But it also means they don't really understand what you are doing, why you are doing it or how you are doing it.  So you need to do a lot of hand holding throughout the process

For these reasons, building clean, pretty interfaces is almost twice as important as actually making sure the technology works.  This is because adoption of technology is very, very low in the government/ non-profit space.  If they don't understand what you've made intuitively (aka without really understanding) they won't use it.  No matter how much money the organization as a whole paid for the software, service or technology.  

So we are going to talk about design estetic, work flow, and a few other things.

###Design Process

Website built for the social justice space need to be as simple as possible.  You can do a max of three things per page, but really you should only do 1 thing.  And each tool should never really do more than 1 to two types of tasks.  It's also important to understand, that no matter how useful a tool or set of tools might be, there is a finite amount of brain space for actually using tools, no matter how much easier the next thing might make someones life.  So, you need to make sure that whatever you build is as useful as possible, even if it's technically very boring.  

In fact, the tool that has had the highest adoption rate since I started working in government is the PDF to CSV tool I touched on in chapter one.  All the machine learning stuff was put into production, but it took 2 years to find the right client - a national organization of folks who came from fortune 500 companies, to understand and make use of those analyses.  So, the point, keep it simple, otherwise no one will use it.

So how should design of websites like this look?  I don't know.  And neither does anyone else.  There are certain rules I've picked up, but in all honesty, you'll need to do an agile iterative design, before you have any idea about what you are going to build or how it's going to look.  If you can add bootstrap, great!  But don't do it until after you've iterated on your design with all the members of your team.  

So how do you do agile in the government or non-profit space?  

1. Find a person who is excited about technology - this is going to be your alpha tester.  He or she will be your companion on the journey to creating something useful.  For me, this was a young woman named Rachel.  Over the past year we've worked together extremely closely.  It hasn't always been fun, but its almost always been productive.  The way our interactions typically work is, I get a requirement from my boss or I pitch an idea.  I explain the idea to Rachel, she gets way too excited and thinks I'll finish it tomorrow, and then I get to work.  Typically later that day I'll have a prototype with a basic flask app and a button.  The button will give her the output from the task and she'll give feedback about the look of the output, the interface and the workflow.  I'll take her notes and iterate on the design.  Usually we'll do this three to five times.

2. Show someone else - Usually by this point, a week or two later, I'll have something that other people will understand and be able to use.  Typically all the design work has already happened with Rachel, since she knows the rest of the team very well.  However, making sure the workflow is intuitive to other folks is important, because it gets their buy in.  Its important to get as much of the teams buy-in as possible.  This ensures that more people will adopt the tool.  Because remember, just because you build, it doesn't mean they'll use it.  Even if its what they asked for.

3. Get by in from management - Its a sad truth, but no matter how good a tool is or how much time its going to save, if your boss doesn't care, it won't get put into production.  So make sure you have his or her approval.  It's also important that they know about the project from the beginning.  So although you have someone else who is working on it, make sure they are onboard with what you are doing.

4. Get ITs buy in - Unfortunately my person situation didn't really allow for this.  So I recommend making friends with IT early on in your time.  Your going to need them on your side if you want to get stuff into production, at least in many government institutions.  Unfortunately, most of the time ITs (preference) is to say 'no' to new projects.  So if you can get ally's here, it will make a world of difference.  Assuming you can convince them to be on your side and actually do stuff that's meaningful, you should run it by them after you tell your boss, but before making the request to put it into production.  If possible show them a prototype.  

So really steps (3) and (4) happen after you've already started the iteration process with your alpha tester, but before you've completed it.  So maybe after the second iteration.  

###Design Examples

Now that we've touched on the design process, let's talk about the design itself.  

###Installation

[flask](http://flask.pocoo.org/) - sudo pip install flask


[bootstrap](http://getbootstrap.com/) - installation of bootstrap is slightly more involved than previous software.  You'll need to either get a bunch of CDNs (content delivery networks) or download the (minified) source directly.  

This simple example shows you how to include the Bootstrap CDNs in a simple HTML page:

```
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

	<!-- Optional theme -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
</head>
<body>

</body>
</html> 		
```

it's also worth noting that we can install bootstrap/jquery via npm or bower.  With the following commands:

bower:
* `bower install bootstrap`
* `bower install jquery` 
npm:
* `npm install bootstrap`
* `npm install jquery`

[angular.js](https://angularjs.org/) - we'll also need either a [CDN](http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js) or we'll need to install angular locally with the command `npm install angular`.  It's worth noting that npm installs packages to a directory rather than globally.  You can do the following if you'd prefer to have certain packages globally:

`npm config set prefix /usr/local`
`npm install -g [package name]`
`which [package name] #testing everything worked` 


###Building our first flask app

Flask is one of the simplest and most useful web frameworks in the world.  This is not only because you can create servers with the absolute minimum number of explicit lines of code, but because it has a ton of extensions that make it robust when necessary, but flexible enough to just get stuff done.  

The following example is done entirely from the python shell:

```
>>> from flask import Flask
>>> app = Flask(__name__)
>>> @app.route("/",methods=["GET","POST"])
... def index():
...     return "Hello there"
... 
>>> app.run()
```

The same app can be found [here](https://github.com/EricSchles/book_tools/tree/master/code/chapter3/basic_flask)

As you can see, writing a very minimal flask app is extremely easy.  And the good news is it continues to be easy for larger apps.  So how does a flask app work?

First there is the flask object - `Flask` - this object creates the context for the running website.  You can add routes to the app context and then run those routes.  A route represents a url path and the action(s) the server will take when a browser visits the page, or more technically when a request is made to the endpoint.  Notice that route takes one parameter by default and lots of optional parameters.  The most common one is methods, which tells the server what kinds of requests the end point should handle.  Typically get requests are for getting html pages or other kinds of data from the server, whereas post requests are for sending data to the server, as is the case with forms.  (You may remember this type of discussion from chapter 1).

Let's do something slightly more complex now.  Doing so will require a few files and some folders.  Here is our file structure:

web_app/
   run.py
   app/
	  __init__.py
	  server.py
	  templates/
	    index.html

It may seem artificial to seperate our application into all these different pieces, but this structure will be very useful once we start using blueprints - a pattern that lets us split up pieces of the web application into different application contexts.  This allows for faster development and better organizational structure at scale.  It also leads us well to understanding the structure of the django framework, which we'll get into soon!

run.py:

```
from app import app

app.run(debug=True)
```

__init__.py

```
from flask import Flask

app = Flask(__name__)

from app import server
```

Basically, __init__.py handles the instantiation of our application context and run.py handles actually running the server.  

The server.py file is where all our routes are going to live for now.  This application will still be very simple - its simply a form that takes in a name and email address and then displays the pair in a list below the form.  While this may be a trival example it illustrates two major tasks in web development - getting data from the server and sending data to the server.  Another important aspect of this application, is the data is persistent, because we make use of a simple database.  

So let's take a look at server.py:

```
from app import app
from flask import render_template,request,jsonify,redirect,url_for
from flask.ext.sqlalchemy import SQLAlchemy

###Models

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Store(db.Model):
    __tablename__ = 'store'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400),nullable=False)
    email = db.Column(db.String(400),nullable=False)

    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return  "<store %r>" % self.name

###Controller

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html",data=Store.query.all())

@app.route("/add_data",methods=["POST"])
def add():
    print "posted data to the server"
    name = request.form.get("name")
    email = request.form.get("email")
    store = Store(name,email)
    db.session.add(store)
    db.session.commit()
    print store
    return redirect(url_for("index"))
```

Here we've split up our concerns into model and controller - this idea of splitting up concerns in this way comes from the model,view,controller pattern.  The view logic lives in the html file, which we will see in a few moments.  The model concerns model our data, telling our database what kind of data should be stored, as well as how that data should be represented.  We express storage via:

```
__tablename__ = 'store'

id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(400),nullable=False)
email = db.Column(db.String(400),nullable=False)

def __init__(self,name,email):
    self.name = name
    self.email = email
```

We model our data as sqlalchemy's general purpose Object Relational Model.  The individual fields are modeled via db.Column.  We then inform the database what to do on instantiate of our record object - with the `__init__` method.  Notice that we don't need to pass an id, it is generated automatically.  The id is good practice and is useful for indexing data, allowing for faster queries, and database tunning generally.  

Now we can explore the other part of our database class:

```
def __repr__(self):
    return  "<store %r>" % self.name
```

Here we make use of the `__repr__` method which will determine the representation of individual objects of our database, assuming we want high level information about the objects.  We can also access individual fields from our objects in the following way:

testing_database.py:

```
from app.server import Store

store = Store.query.all()[0] #get any old object.
print store.name
print store.email
```

Notice that we can access the individual fields, and so, `__repr__` is more of a notational convenience more than anything else.  This way we can know what object we are dealing with, without having to deal with accessors.

Now let's look at the controller:

```
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html",data=Store.query.all())

@app.route("/add_data",methods=["POST"])
def add_data():
    print "posted data to the server"
    name = request.form.get("name")
    email = request.form.get("email")
    store = Store(name,email)
    db.session.add(store)
    db.session.commit()
    print store
    return redirect(url_for("index"))
```

Here we don't have a ton of new stuff.  Notice that we only expose a `POST` method for our `add_data`-route, which will be used for submitting our form data.  Notice that I name the route the same as the method, this is good practice, as we will see, for `url_for`, which resolves method names to their url.

At this point, it makes sense to bring in the html to understand the interaction between the view and the controller:

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>

<form method="post" action="{{url_for('add')}}">
<label>Name:</label><input type=text name=name>
<label>Email:</label><input type=text name=email>
<input type=submit>
</form>

<ul>
{% for datum in data %}
 <li> {{datum.name}} , {{datum.email}} </li>
{% endfor %}
</ul>

</body>
</html>
```
