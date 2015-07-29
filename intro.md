#Tools For Social Justice in Python
__By__
_Eric_ _Schles_


##Organization of the text

###Introduction
* The intention of the text/thank you 
* Strategies for getting stuff done
* prerequisite knowledge (and resource to learn said prerequisite knowledge)
* outline of text/overview of text 

###Chapter 1
working with data for non-profits and government
* web scraping
* PDF to csv
* data cleaning techniques
* optical character recognition - hard
* named entity resolution with machine learning

###Chapter 2
Analyzing data for government and non-profits
* finding optimal solutions to organizational issues:
    * choosing the optimal number of beds for a homeless shelter - hard
* doing social network analysis to catch bad guys and make connections
     * graph based algorithms - easy?
* Looking for money laundering in financial data - easy?
* analyzing audio records for red flags with time series analysis - easy?

###Chapter 3
Visualizing data for analysts and to find patterns and creating interfaces
* gis systems for free - easy
* c3,d3, and vincent - easy
* time series analysis in action - easy
* web dev in flask, boot strap, and angular.js - easy

###Chapter 4
Searching across massive data sets
* facial recognition and facial comparison - building a cbir - easy
* searching across text in mass - easy
* classifying text - easy
* multithreading applications for faster processing - easy
* using Hadoop and spark for search - easy

###Chapter 5
Build the system I pitched to OAG - easy
Finding patterns with disparate data
* bringing together closed and open data to build systems
Three example systems in this chapter



##Introduction

###The intention of this text/thank you

The intention of this book is to explain the interested reader how to use computer science to solve social problems.  To build systems and change minds and hearts.  Often times those interested in social justice are not technologists and so they are unaware of what technology can do to make their work easier and more effective. 

This book is divided into five chapters, each one touching on a specific theme.  Each theme is intended to provide background and code on how to do one type of task.  These tasks were culled from the many projects I have participated in, in the social justice/non-profit/government space.  The intention of this guide is to teach you how to recreate the tools I have made but more so, to teach you, the developer, how to recreate the mindset I used to make these tools.  I selfishly want to help the world, to make it a place that is more fair and balanced.  A place where everyone is guaranteed freedom from opression or violence.  A place where love wins over fear, not in every instance, but on average and increasingly so.  In a way this means building systems where such guarantees are possible.  Except the cogs of the system are people and social organizations, not machines.  The intention of this book is to teach you how to construct the machinery of the morality.  And to inject justice, freedom, voice to those most in need and in suffering.  

It is no simple task that we embark on, but that also doesn't mean it has to be hard.  Together, with your intention, and my knowledge, I believe we can make a difference together.  I only hope that the lessons I have learned can be helpful in your work, whatever it may be.  In computer science we spend so much time perfecting the ability to solve difficult, previously in tractable problems.  We seek elegance of form in our solution.  We try to build clean obvious solutions.  Selfishly it is my hope that we can apply such systematic thinking, where possible, to the social problems of the world, and in doing so, form a better tomorrow for us all.

This text would not be possible without my mentors, friends, family, and collaborators.  So to my parents Marc and Andrea, I say thank you for embuing me with a social compass, and for believing a life of service is the most fulfilling one.  To my friends, I say thank you, you are far to numerous to name, but you know who you are.  If not for you, I would have never made it through school or life, you are oxygen, and I hope you all know that.  To my mentors, Ethan Mann, James Javor, Ellen Eurbanek, the late Samuel Schack, John Temple, and Andrew Raiseji you have my deepest thanks.  If not for your guidance, and support I would have never found the direction that has led me to this point.  It is my only hope that I can be half the mentor that each of you has been to me.  And finally to my collaborators, I say thank you for your partnership and fraternity in this fight for a better tomorrow.  I will name each of them throughout the text and so their names and organizations are merely listed here.

* Freddie Andrade wikitongues
* Daniel wikitongues
* Miguel Code in mexico - fix this (get spanish name)
* Marianne Belloti Exversion
* John Temple Manhattan District Attorney's Office Human Trafficking Response Unit
* Genna ECPATUSA
* Janai Smith ECPATUSA
* Geofrey Digital Ocean
* Phil Self Employed
* Lior Shahverdi Self Employed
* Alan NYU
* Tim Savage NYU
* Steve EPA

###Strategies for getting stuff done
ToDo - write up the strategies for getting around obstacles in local government and add this to the introduction.


###Prerequisite Knowledge (and resource to learn said prerequisite knowledge)

The intention of this text is to cover a lot of ground quickly.  However, I want this text to be accessible to those who don't know everything.  Here are some of my favorite guides to get all the prerequisites out of the way.  

list of prerequisites:

For Beginners:
* [Codecademy](https://www.codecademy.com/tracks/python)
* [Khan Academy Python](https://www.youtube.com/playlist?list=PLJR1V_NHIKrCkswPMULzQFHpYa57ZFGbs)

Transition from Beginner to Intermediate
* [Learn to Code the Hard Way](http://learnpythonthehardway.org/book/)
* [Python Open Book Project](http://www.openbookproject.net/thinkcs/python/english2e/index.html)

Intermediate
* [Data Structures and Algorithms in Python](http://interactivepython.org/runestone/static/pythonds/index.html)
 
Intermediate and Advanced Topics:

More Python Resources:
* [General Set of Guides for Python](http://docs.python-guide.org/en/latest/intro/learning/)

Data Science Resources:
* [Set of Guides for Learning Data Science (Mostly Free)](http://datasciencemasters.org/)
* [A list of Tools for Data Science](http://www.mastersindatascience.org/blog/open-source-tools-for-big-data-analysis/)

Web Dev:
* [A list of web dev tools and learning resources](http://tutorialzine.com/2014/09/50-awesome-tools-and-resources-for-web-developers/)
* [A curated list of Web Dev Guides](https://www.bento.io/)

Chapter Specific Prerequisites

Chapter 1:

ToDo

Chapter 2:

ToDo

Chapter 3:

ToDo

Chapter 4:

ToDo

Chapter 5:

ToDo

References:

[Thomas Levine's personal Blog](https://thomaslevine.com/)
[Aaron Schumacher's personal Blog](http://planspace.org/)
[Data Science 101](http://101.datascience.community/)
[R-Bloggers](http://www.r-bloggers.com/)
[Hardcore currated list](https://lobste.rs/)
[James Powell's Blog](http://seriously.dontusethiscode.com/)

####A quick note on installation

A lot of the tools we'll be using throughout this book will rely on pip, so we'll download and install that now.  From time to time we'll need python packages that don't have working pip repos (at the time of this writing) and so alternatives will be presented for those libraries.  

To get pip head over to [get-pip.py](https://bootstrap.pypa.io/get-pip.py) simply save the file as get-pip.py.  The run sudo python get-pip.py (on ubuntu or mac) or run python get-pip.py with a administrator rights (on windows).

####Github for this book

All the source code for this text can be found on the books associated github site.  Here you'll find a list of what code belongs to what sections:

Chapter1:

Working with GETs and POSTs - `making_requests.py && test_server.py`

#Chapter 1 - Working With Data For Non-Profits And Government

The biggest problem facing government agencies and non-profits today is data.  These problems stem from cleaning, storing, maintaining and sometimes even accessing this data.  Lots of entities have been slow to the technology revolution and often they don't have basic functionality like search.  Much of the data government deals with is either trapped in emails, pdfs, word documents, or pictures.  This means these documents are not searchable and aren't easily capable of becoming searchable.  Of course, many, many solutions exist to this problem, but often times getting such a solution installed is a herculean task, taking many many years.  Therefore writing your own solution is usually going to be faster.  This type of task addresses our first strategy to being effective in government, hack around obstacles.  

For whatever reason, I've found that government administrators are much more comfortable with having python on their machines than a given open source technology.  My guess is this is a mix of fear and misunderstanding of open source technology in general, but I can't be sure exactly why.  In any event, I've found myself waiting months or even sometimes being told a flat out 'No!' to installing specific open source projects.  And therefore, I've had to come up with my own solutions to many well solved problems.  This certainly isn't the case for every government institution or non-profit, but from what I understand talking to other technical colleagues across local government, it seems to be more the rule than the exception.  

The intention of this chapter is to give you methods of hacking around such artifical obstacles as access to data that is already publicly available, search across data, poorly formed data, and data trapped in images.  We'll address these obstacles with the following tools:

* Web Scraping
* Turning PDFs into CSVs
* Data Cleaning Techniques
	* Named Entity Resolution with Machine Learning
* Optical Character Recognition

##Web Scraping

Web scraping is the ability to programmatically store and process data from API's, websites, RSS feeds, and other content that exists on the internet.  The steps usually involve two things - download the relevant content locally and then parse that content, extracting the relevant information.  

There are many great blog posts, tutorials, and tools for doing web scraping.  Here we'll touch on my three of my favorite: 

* [Python's requests Library](http://docs.python-requests.org/en/latest/)
* [Python's lxml library](http://lxml.de/)
* [Python's Selenium library](https://selenium-python.readthedocs.org/) & [Phantom.js](http://phantomjs.org/)

###Installation

####Mac OSX or Ubuntu

sudo pip install -U requests lxml selenium

####Windows

with administrator rights:

pip install -U requests lxml selenium

###Getting started with requests

The requests library is extremely powerful and very high level.  It can be used for a whole bunch of things.  Before we talk about how we use it, let's talk about some reasons why we'd use it.  The common reasons I've seen for using requests is there is some data served somewhere on the internet that people at your organization care about.  For my work fighting slavery, we've often wanted to store the content of a website we think is encouraging or creating human trafficking.  We want to do this for a few reasons, but the most important one is to gather complete and robust evidence because often times this data can be deleted, lost or destroyed.  If that happens then a vital piece of an investigation may be lost.  Another common reason I've seen is for collecting statistics that another website posts, but that isn't publicly available in another format easily.  The other big reason only happens in large government agencies.  This is the case when a certain process publishes regular reports from a database, but you can't find anyone who has access to the database, but you need the data.  

There's one common theme here - there is data that is publicly or semi-publicly available that you'd like to be able to manipulate or store locally, and this data is updated overtime.  

 The requests library allows you to do some very important things, we'll only talk about two of the methods in the library - `GET` and `POST`.  It is assumed that you already know object oriented programming, so if you don't please go check out the resources I listed above so that you know how classes, objects, and data structures work.  

 ####Working with GETs and POSTs

 __Note__: For this section of the text please refer to `making_requests.py` and `test_server.py` in chapter1 in the github repo.

 A `GET` request is one that asks the server for some data.  A `POST` request is one that sends some data to the server.  They are easily to do in the requests library and have specific uses.

 The canonical `GET` request is something like visiting a web page - the html that is rendered by your browser was by a `GET` request (more often than not).  

Here's how that method might look:

```
import requests
r = requests.get("https://www.google.com")
``` 

This request returns an object - which we've named r, short for response.  This is a classical pattern called request, response and you'll find it in other places, like javascript MEAN stack applications.  There are a number of properties that the response object returns.  The most important ones are: 

* text - stores the html of the page as a string
* url - stores the url of the request
* content - stores the content of the request, in case we are dealing with something other than html like a pdf
* raw - the same thing as content more or less, but there is a difference in practice, although I'm not sure what exactly.  Best to try content and if you don't get back everything you wanted, try raw.
* headers - the headers of the request.  

You'd access this information in the following way:

```
import requests
r = requests.get("https://www.google.com")
print r.text
print r.url
print r.content
print r.raw
print r.headers
```

A `POST` request is one that sends data to the server.  Since I don't want to have people sending the same fake data to some website, I wrote my own test server for this example and the remainder of the section.  

So you'll need to get the github repo - `https://github.com/EricSchles/tools_for_social_justice` which you can get by typing:

`git clone https://github.com/EricSchles/tools_for_social_justice.git`

then navigate over to `tools_for_social_justice/code/chapter1/`.  From there you'll be able to run the server with `python test_server.py` and all the examples with `make_requests.py`.  

So go ahead and run the server and then the following code will work:

```
payload = {"username":"eric","pass":"1234"}
r = requests.post("http://localhost:5000/form",data=payload)
```

This request will post the following data - `"eric"` and `"1234"` to the form, which is pretty neat!  Often times you'll need to log into certain government websites, before you can access their data and this will allow you to do just that.  Other uses include automatically filling out forms for surveys - say you're unit needs some piece of software and the agency happens to be sending around a suggestion form, you can write the data so that it's clear that you really want this one specific thing and then pass it around to all your coworkers to run this script.  Just make sure you get your bosses approval first!  But your coworkers will love you for this!  I've spent way too much time filling out internal surveys just to drop the hint that our unit needs one specific thing.  

I do want to note, that not all websites will allow you to pass credentials and then scrape their content, sometimes a web page is generated dynamically, sometimes a website will pass back a cookie, tracking your state while accessing the content of the website.  We'll address each of these cases as well, but this is the simplest form of submitting data to a website.

An important thing to note is, the data here - called payload is sent after the html page is loaded, by the server.  And so it makes sense that a dictionary is passed - the keys correspond to the names of the fields in the html page, the values, the actual data being passed to the form.  

When making use of an api that requires credentials, we'll need to pass a different keyword - auth (instead of data).  This will send the credentials along, before the html page is loaded.

```
data = ('admin','1234')
r = requests.get("http://localhost:5000/secret-page",auth=data)
```

Some important differences to note - 1st we pass a tuple - the credentials listed in order.  2nd we use the `auth` keyword to pass the data.  3rd we make use of a get request, because we want to get some data from the server, rather than sending some form data to the server.  

The next example is that of sending files via a form to the server.  This can be extremely powerful, if you know you have some internal web service and 500 files that need to be processed.  Perhaps classically this service only processed one file at a time.  Rather than having to track down the maintainer of this service, if they are even still around, it's far easier to have python just send all the files across.

This simple example illustrates how to send a file via post request.

```
files = {"file": open("report.csv","r")}
r = requests.post("http://localhost:5000/get_csv",files=files)
```

Notice that this is a dictionary, where the key corresponds to the name of the input form and the value corresponds to the file in question.  For pdfs and microsoft documents you can use `open([filename],"rb")`.  This stands for read binary.  

####Parsing HTML

Now that we know how to get and send data programmatically, we are ready to start being selective about what we download and keep or write a web crawler.  Web crawlers are extremely powerful for mapping every page of a website and infact, I've done just this to forensically download and store websites over time, to be used as evidence of human trafficking.  Other uses exist in the investigative world, like navigating the deep web.  


```
