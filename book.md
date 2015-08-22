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
	* named entity resolution with machine learning
* optical character recognition - hard

###Chapter 2
Analyzing data for government and non-profits
* finding optimal solutions to organizational issues:
    * choosing the optimal number of beds for a homeless shelter - hard
* Raising funds, finding bad guys, with targeted advertising:
	* raising funds - predictive marketing
	* finding bad guys - understanding your population with descriptive statistics
* doing social network analysis to catch bad guys and make connections
     * graph based algorithms - easy?
* Looking for money laundering in financial data - easy?
* analyzing audio records for red flags with time series analysis - easy?

###Chapter 3
Visualizing data for analysts and to find patterns and creating interfaces
* web dev in flask, bootstrap, and angular.js - easy
* gis systems for free - easy
* c3,d3, and vincent - easy
* time series analysis in action - easy

###Chapter 4
Searching across massive data sets
* facial recognition and facial comparison - building a cbir - easy
* searching across text in mass - easy
* multithreading applications for faster processing - easy
* using Hadoop and spark for search - easy

###Chapter 5
Build the system I pitched to OAG - easy
Finding patterns with disparate data
* bringing together closed and open data to build systems

Three example systems in this chapter
Investa_gator/alert system

twilio system
 - setting up a hotline
 - diaster recovery/mass text message alerts

bring together everything in the book to build one giant automated attack system


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
* Rob Spectre - Twilio

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
* [A talk on named entity recognition](http://www.slideshare.net/BenjaminBengfort/a-primer-on-entity-resolution)
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

* [Thomas Levine's personal Blog](https://thomaslevine.com/)
* [Aaron Schumacher's personal Blog](http://planspace.org/)
* [Data Science 101](http://101.datascience.community/)
* [R-Bloggers](http://www.r-bloggers.com/)
* [Hardcore currated list](https://lobste.rs/)
* [James Powell's Blog](http://seriously.dontusethiscode.com/)

###A quick note on installation

A lot of the tools we'll be using throughout this book will rely on pip, so we'll download and install that now.  From time to time we'll need python packages that don't have working pip repos (at the time of this writing) and so alternatives will be presented for those libraries.  

To get pip head over to [get-pip.py](https://bootstrap.pypa.io/get-pip.py) simply save the file as get-pip.py.  The run sudo python get-pip.py (on ubuntu or mac) or run python get-pip.py with a administrator rights (on windows).

###Github for this book

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
import requests
import lxml.html
from unidecode import unidecode
from sys import argv

website = argv[1]
r = requests.get(website)
html = lxml.html.fromstring(unidecode(r.text))
print html.xpath("//a/@href")
```

In this simple example we see the power of web parsing, in its simplest form - grabbing all the links from a web page.  Once we have a web page in memory, we transform the ascii characters into something python can understand, via unidecode, and then loading the html into the lxml tree data structure.  Once we've parsed all the tags via lxml's fromstring method, we are free to make use of xpath - a micro language that will allow you to quickly and efficiently traverse a tree to query for certain peices of information, in this case all the hyper links in an html page.  

While xpath as a language is far too deep in terms of length to go into in detail, we'll cover a few features here:

`//` - searches the whole tree for the following tag, from the root of the tree
`/` - search from the relative node that is referenced so `//a/p` will search after all the a tags, and `/a` searches only the top level of nodes
`/a/@href` - searches for a tags with the href attribute
`/a/p[@id="hello"]` - searches for all a tags with `id="hello"`

If the xpath language isn't familiar to you I'd recommend the following guides:

* [w3schools](http://www.w3schools.com/xsl/xpath_intro.asp)
* [mozilla guide](https://developer.mozilla.org/en-US/docs/Web/XPath)

####Crawling the web

One of the great things of python is how readable and compact you can make the code.  The following piece of code is a fully capable web crawler (albeit without any bells or whistles).  A slightly more robust version of this (complete with a database) lives on the github repo for the book [here](https://github.com/EricSchles/book_tools/blob/master/code/chapter1/crawler.py)

```
import requests #sudo pip install requests 
import lxml.html #sudo pip install lxml.html
from unidecode import unidecode #sudo pip install unidecode

def links_grab(url):
    r = requests.get(url)
    html = lxml.html.fromstring(unidecode(r.text))
    return html.xpath("//a/@href") + [url] #ensures the url is stored in the final list

def crawl(base_url,start_depth=6):
    return crawler([base_url],base_url,start_depth)

def crawler(urls, base_url, depth):
    urls = list(set(urls))
    domain_name = base_url.split("//")[1].split("/")[0]
    url_list = []
    for url in urls:
        if domain_name in url:
            url_list += links_grab(url)
    url_list = list(set(url_list)) #dedup list
    url_list = [uri for uri in url_list if uri.startswith("http")]
    if depth > 1:
        url_list += crawler(url_list, base_url, depth-1)
    urls += url_list
    urls = list(set(urls))
    num_urls = len(urls)
    return url_list
```

So let's break down the code.  The `links_grab` function should look familiar, since we made use of it in the last example.  Notice the small difference - the return statement is adding two lists together, which is why [url] is stored as a list.  

Next we'll look at the crawler function.  

The first line - `urls = list(set(urls))` deduplicates the urls as they are passed in, this ensures no url will be scraped twice, which would be redundant.  

The next important line is - `if domain_name in url:` - this ensures that we are only grabbing content from one domain at a time.  I include this because otherwise our list of urls will grow exponetially fast and by the fact that we aren't trying to necessarily re-implement the google crawler.  Typically in investigative work, we only care about grabbing all the html for a single domain, rather than multiple.  Of course, there will be some circumstances when you want all the domains linked to a website, if that is the case, simply remove this line.  You can of course add further customization - simply by ignoring certain domain names.  Below is a modified crawler method that ignores popular websites you are unlikely to care about when trying to store neifarious websites:

```
def crawler(urls, base_url, depth):
    domains = ["www.google.com","www.yahoo.com","www.linkedin.com","www.github.com"]
    urls = list(set(urls))
    url_list = []
    for url in urls:
        if not any([domain in url for domain in domains]):
            url_list += links_grab(url)
    url_list = list(set(url_list)) #dedup list
    url_list = [uri for uri in url_list if uri.startswith("http")]
    if depth > 1:
        url_list += crawler(url_list, base_url, depth-1)
    urls += url_list
    urls = list(set(urls))
    num_urls = len(urls)
    return url_list
```  

Here we simply create a new list of domains and if any of them are found, we don't scrape those urls.  The assumption is that you don't start from one of the urls on the no-scrape list.  

Once we've scraped all our links we dedup again with `url_list = list(set(url_list)) #dedup list` and then make sure all our urls are reachable via their uri `url_list = [uri for uri in url_list if uri.startswith("http")]`.  Many href's refer to relative paths for websites.  Since this is just an introductory example, I don't include the code to resolve this here, however in the github repo, I have all the necessary added steps to resolve relative urls.  I have to warn you however, this makes things very slow.  You'd be surprised how many urls you can get from a single scrape.  

Notice the next lines `if depth > 1:` and `url_list += crawler(url_list,base_url,depth-1)`, this is the recursive step and sort of the heart of the engine.  Since we are moving through the urls recursively, scraping new links from the current step, our list of urls will get big fast.  We can think of the structure of a single scraping like a b-tree, where the number of edges at a given level corresponds with the number of links on a page, and each node being the actual html page, storing said edges.  This structure shows just how exponentially large our b-tree grows, often very big very fast.  It would be an interesting study to look at how the number of links grow from page to page on average for different types of websites, allowing us to understand an average bounding on the time complexity of a type of scrape.  But enough about the how, let's talk about the why.

Often times we need to scrape a set of pages for a few reasons:

1) To get information trapped from some database that you are supposed to have access to, but don't, mostly because the person who runs said database is being difficult and doesn't want to give you a direct feed.  However the information is of course, published publicly in a far less machine readable format.  


This is an example of hacking around obstacles, something you'll need to do often if you decide to work for the government or really any non-profit.  I'm not sure why folks are stubbornly unhelpful in these roles, but usually they are.  


2)  To grab information for an investigation.  Often times on the sex trafficking world traffickers will post to a website like backpage.com but have their own websites that you can link to.  The content on these smaller websites will often change, sometimes very regularly, and sometimes not at all.  It is important to an investigation to know all the people that are featured on a given website of this kind, and so being able to readily store such information is of paramount importance.  


3)  To do market research.  An unfortunate part of the non-profit space is grant writing.  This takes up a lot of time for many NGOs and non-profits, so knowing what everyone else in the space is saying with real-time accuracy is often a big deal.  Being able to scrape the other folks in the space becomes an important part of the grant writing process - knowing not only what they are saying, but what they are not saying.


4)  Scraping other government entities.  If you thought your IT department was bad, wait till you meet the IT folks in other government agencies, these are typically the least helpful people possible.  If your IT staffer decides he/she doesn't like you and doesn't want to help, at least you can escalate things to superiors so that they have to do it, if other people in other IT departments don't like you, there is no path forward, ever.  But often when working on a problem with a social justice theme, you'll need the information that other government agencies are using.  Thanks to open data standards that are being forced on many public agencies, for the first time, you'll have the ability to actually circumvent this difficult people, so that you can actually do your job!  Often times, you'll be able to make the scraping happen, so you can get your work done.


##Turning PDFs into CSVs

This next section really addresses this last point from the previous section - working with government data from other entities.  As I've already said, many government institutions will have to release a bunch of their data to the public, in an attempt to create a more open and transparent government.  Of course, this has lead to a ton of problems.  Partially because many government instutions aren't really equiped to do that, from a technical stand point.  And so, often what you get, is folks just publish static pdf documents to the web and think they are being open and transparent.  One of the most important things open governance needs is the ability to make this data machine readable.  However, this is likely a far off dream, so we are going to hack around it.  

The uses of machine readable data across government are limitless, but here are a few my favorite ideas - 

1. Creating citizen based analysis to show however government could be more effective:
	* Maps showing you were all the safest parks are based on crime data
	* High level financial analysis showing where and government dollars are actually spent, as well as how they could be spent better
	 
	
2. Creating citizen based feedback loops showing government how they could better govern:
	* Active voting from quarter to quarter, based on the performance of a specific agency, which partially determines funding level


Both of these could be accomplished via an API, number (1) from an api-GET request and number (2) from an api-POST request.  Thats it.


In lew of such a fully functional API and having to work with PDFs isn't the end of the world.  In this section we'll cover how to parse PDFs and give you stragies for getting the information you want.

The first strategy involves finding static text that doesn't change from document to document, this is typically useful for quarterly reports that are generated from a database.  Because parts of the text don't change, you can use these as relative offsets to only process the parts of the document you care about.  I'll refer to these pieces of unchanging text as invariants or text invariants.  

Once we have the invariants figured out, we'll need to understand the structure of the data or text we want.  This is typically a table, or a chart.  Ofcourse, from time to time we also want some text, but this method generalizes nicely to that case as well.  

###Installation

Pandas - `sudo pip install pandas` or `sudo apt-get install python-pandas` #ubuntu only
Poppler-utils:
 * On ubuntu - http://poppler.freedesktop.org/
 * On Windows - http://blog.alivate.com.au/poppler-windows/

Note for windows you'll need to set the environment variables or pdftotext.  For information on how to do this please see [this guide](http://www.itechtalk.com/thread3595.html)

The following piece of code can be found in the chapter1 section of the github:

```
from subprocess import call
from sys import argv
import pandas as pd
def transform(filename):
    call(["pdftotext","-layout",filename])
    return filename.split(".")[0] + ".txt"

def segment(contents):
    relevant = []
    start = False
    for line in contents:
        if "PROSECUTIONS CONVICTIONS" in line:
            start = True
        if "The above statistics are estimates only, given the lack" in line:
            start = False
        if start:
            relevant.append(line)
    return relevant

def parse(relevant):
    tmp = {}
    df = pd.DataFrame()
    for line in relevant:
        split_up = line.split(" ")
        # a row - 2008 5,212 (312) 2,983 (104) 30,961 26
        split_up = [elem for elem in split_up if elem != '']
    
        if len(split_up) == 7:
            tmp["year"] = split_up[0]
            tmp["prosecutions"] =split_up[1]
            tmp["convictions"] = split_up[3]
            tmp["victims identified"] = split_up[5]
            tmp["new or ammended legistaltion"] = split_up[6]
            #print tmp
            df = df.append(tmp,ignore_index=True)
    return df

if __name__ == '__main__':
    txt_file = transform(argv[1])
    text = open(txt_file,"r").read().decode("ascii","ignore")
    contents = text.split("\n")
    relevant = segment(contents)
    df = parse(relevant)
    df.to_csv("results.csv")
```

This code parses the pdf - trafficking_report.pdf which can also be found in the github.  This is a very long report, but what we care about is one table in particular (by way of example).  This table can be found on page 45 of the report and it details arrest details about human traffickers internationally.  

Let's walk through each of the methods, which are defined in the order they are called.

```
def transform(filename):
    call(["pdftotext","-layout",filename])
    return filename.split(".")[0] + ".txt"
```

The transform method calls pdftotext, a command line utility that transforms a pdf into a .txt document.  Notice the use of the layout flag which preserves the formatting as much as possible from our pdf file, this is crucial to ensuring our .txt document will be easily parsable.

```
def segment(contents):
    relevant = []
    start = False
    for line in contents:
        if "PROSECUTIONS CONVICTIONS" in line:
            start = True
        if "The above statistics are estimates only, given the lack" in line:
            start = False
        if start:
            relevant.append(line)
    return relevant
```

In the segmentation step we find the text invariants that start and end the section of the document we wish to parse.  Here the start  invariant is `"PROSECUTIONS CONVICTIONS"` and the end invariant is `"The above statistics are estimates only, given the lack"`.  What's returned is a simple dictionary of the relevant lines of text from the transformed .txt document.

```
def parse(relevant):
    tmp = {}
    df = pd.DataFrame()
    for line in relevant:
        split_up = line.split(" ")
        # a row - 2008 5,212 (312) 2,983 (104) 30,961 26
        split_up = [elem for elem in split_up if elem != '']
    
        if len(split_up) == 7:
            tmp["year"] = split_up[0]
            tmp["prosecutions"] =split_up[1]
            tmp["convictions"] = split_up[3]
            tmp["victims identified"] = split_up[5]
            tmp["new or ammended legistaltion"] = split_up[6]
            #print tmp
            df = df.append(tmp,ignore_index=True)
    return df
```

The final section is the parse method.  Here we create a dictionary which will be appended to the pandas DataFrame that we'll make use of.  The reason for storing things in a pandas dataframe is because of the ease of transformation to other persistent file stores such as CSV, EXCEL, a database connection, and others.  Notice that inside the loop we split up the line by whitespace, since this is a table, we should expect tabular data to appear in the same position on different lines.  Also notice that we expect the size of each split up line to be of length 7.  Not that this does not capture a few of the lines in the original pdf, it is left as an exercise to handle these minor cases.  Length is not the best metric for ensuring you are processing the correct information, but the intention of this code is to be as readible as possible, not necessarily as sophisticated as possible.  Other ways you can check to ensure your scraping the correct text is with regex, checking for certain character invariants that should appear on every line, or by using advanced machine learning techniques which we will talk about in the next section.  Finally, the tmp dictionary is assigned each of the values from the table and appended to the dataframe.  Notice that we only need to create tmp dictionary once and then simply overwrite it's contents on each loop through the relevant content.  Then we simply return the dataframe to main.  Here a single line is used to send the dataframe to a csv: 

`df.to_csv("results.csv")` 

And we are done!

There are other, more elegant ways of parsing pdfs, like those found in [this chapter](https://automatetheboringstuff.com/chapter13/) of automate the boring stuff.  Unfortunately, using a library like PyPDF2 won't work in all cases.  So while my method is certainly not elegant, it is robust and will work 99% of the time.  

##Data Cleaning techniques

Now that we know how to handle PDFs under the best possibel scenario, when there are no Optical Character Recognition errors, its time to deal with slightly less than ideal situations, IE when there are mistakes in your data.  In the typical large company setting data isn't entered the same way consistently, which is an annoying problem, however for that we have things like named entity recognition, which we'll get into.  What I'm talking about is when your data is plain and wrong.  Here's an example of what I mean:

A row is supposed to say:

For check number ending in 7519: 

But it actually says:

F0e c$#ck namb   ending in 7%@!:

How the heck are you supposed to handle this situation?!  This is what actually happened to me while working for the manhattan DAs human trafficking response unit.  We'd get a ton of documents from subpoena compliance, but we could only afford an absolutely terrible OCR solution and so the .txt documents hand BOAT loads of errors just like the above.  And here's the truly frustrating thing, they were never consistent.  The OCR solution would mess things up, often differently, for the same words.  And so you'd never get consistent results.  This is really bad for two important reasons:

1. Because it means my invariant scheme falls apart :(((( <- the many chins of sadness rained down upon me the day I realized this.

2. Because it means your data will be inconsistent and incorrect in your CSV :((((( <- even more chins of sadness, I had to stress eat to cope with the level of depression and thus became even fatter.

So, how do we get around this?  Unfortunately there is no one size fits all answer, but there are lots of things you can do:

Let's say you know that there are certain words that will never appear in a line with something you do care about, but this data is being collected, I.E. you have extra data.  Then you could do something like this:


```
def parse(relevant):
    tmp = {}
    df = pd.DataFrame()
	to_avoid = [
		"Hard to see",
		"weird",
		"Something else you want to avoid"
	]

    for line in relevant:
    	if any([elem in line for elem in to_avoid]):
            continue

        split_up = line.split(" ")
        # a row - 2008 5,212 (312) 2,983 (104) 30,961 26
        split_up = [elem for elem in split_up if elem != '']
    
        if len(split_up) == 7:
            tmp["year"] = split_up[0]
            tmp["prosecutions"] =split_up[1]
            tmp["convictions"] = split_up[3]
            tmp["victims identified"] = split_up[5]
            tmp["new or ammended legistaltion"] = split_up[6]
            #print tmp
            df = df.append(tmp,ignore_index=True)
    return df


```

With this you can keep a list of all the terms you want to avoid and simply not process any line that has this term you know will cause problems.  So now we can handle the case when we have too much data, what happens when we miss some data?

For that we'll need to account for all the variations of a given starting or closing phrase:

```
def segment(contents):
    relevant = []
    start = False
    starting = [
    	"PROSECUTIONS CONVICTIONS",
    	"PROSECUTIONS",
    	"CONVICTIONS",
    	"CONVICTION$",
    	"C0NV1CT!ONS"
    	]
    ending = [
        "The above statistics are estimates only, given the lack",
        ", given the lack",
        "The above statistics are estimates",
        "statistics are estimates"
        ]
        
    for line in contents:
        if any([elem in line for elem in starting]):
            start = True
        if any([elem in line for elem in ending]):
            start = False
        if start:
            relevant.append(line)
    return relevant
```

Here we can see employing a similar trick.  Every time we encounter a new type of OCR error, we handle it in specific.  However, this likely doesn't generalize well, here we enter named entity recognition to generalize out this technique further, making it more flexible and effective.


##Named Entity Recognition

So far we've covered a somewhat hacky way of converting things that should be the same to things that are treated the same, but we didn't actually transform anything.  Named entity recognition is the practice of taking techniques from machine learning and other data processing techniques, and using them to convert text that looks different but has the same semantic meaning.  The most common example of this is disambiguating addresses.  There are hundreds of ways to write a single address, which you wouldn't think, but account for the fact that people misspell things and this becomes very plausible.  And so you need a way to make sure all of the different ways you can write 1234 Fake st., New York, NY, 10013 are all the same thing.  Of course, the first thing to do is decide on a canonical representation and then make sure everything that should be that thing, appears the same way.  

Since named entity recognition is actually a very, very diverse set of techniques, we'll just touch on a few of each.  You can see a more complete list of these techniques in [this great lecture by Benjamin Bengfort](http://www.slideshare.net/BenjaminBengfort/a-primer-on-entity-resolution).

###Installation

* [Dedupe](https://github.com/datamade/dedupe) - sudo pip install dedupe
* Potential dependency for Dedupe: sudo pip install zope.interface
* [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) - sudo pip install fuzzywuzzy
* [Distance](https://pypi.python.org/pypi/Distance/) - sudo pip install Distance
* [PyBloom](https://pypi.python.org/pypi/pybloom/1.0.2) - sudo pip install pybloom
* [NLTK](http://www.nltk.org/) - sudo pip install -U nltk; python -c "import nltk; nltk.download()"
* [scikit-learn](http://scikit-learn.org/stable/) - too long for one liner here's [a guide](http://www.astroml.org/sklearn_tutorial/setup.html)
* [Jellyfish](https://pypi.python.org/pypi/jellyfish/0.5.1) - sudo pip install jellyfish

Together the above packages represent throwing the preverbal kitchen sink at the problem.  Yes, a lot of people have spent time and energy making sure that the preprocessing of data was easy.  Sadly, this topic is still daunting for first timers.  Mostly because there are so many tools and a lot of it comes down to a matter of taste.  This is in part because there are so many ways to do data transformations and different people will be more or less comfortable with different techniques depending on their background.  They'll all agree on some set of techniques, but the ways to get there are many.

It isn't essential that you pick a favorite, or that you use any of the above packages.  In fact, all of the transformations you could want to do can with the techniques I already showed you in the last section.  However, that doesn't mean this will be the most performant or accurate way to do things, and that's what these techniques are for.  So you don't have to reinvent the wheel.

First we'll talk conceptually in this section, about the techniques you can use.  And then we'll play with each of the libraries, showing very basic examples.  I don't want to be exhaustive about how to do everything or walk you through all of the examples each of these libraries provides, because this isn't a book solely on machine learning, it's a book about getting stuff done.  And so if you feel like you'd be better served simply knowing these libraries exist and getting your hands dirty, I'd encourage you to do so.

Also, it's worth noting that much of this section is lifted from the Benjamin Bengfort lecture listed above.


So let's get some definitions going:


* Deduplication - Cluster records that correspond to the same real world thing
* Canonicalization - Creating one representation for each real world entity
* Record Linkage - Match records from one record store to another (typically a CSV or a database table)
* Referencing - Match records to a look up table that has already been processed
* Normalization - make everything look the same (no capitalization, no extra spaces, etc.)

As you can see these are all pretty standard tasks.  But really they are just ways about talking about one thing, how do we tell when something is the same?  And what does being the same mean, really?  

The simplest form of checking for similarity is via various distance metrics, in written language.  So how do we define distance?  It's clearly not topological, at least not in the strict mathematical sense.  We can't do an L1 or L2 norm.  We can think of numbers in two space or three space.  Or can we?  Even if we could, it probably wouldn't make much sense.  

Instead, let's prepose that we look at things like the length of two words, the beginning of two words, the number of characters that are common to both words, how similar two words sound when pronounced and their colocation in reference to other words throughout a text.  These will form the basis for our understanding of 'distance' in the land of words.

###Edit Distance

First we'll look at edit distance - the number of characters you'd have to change in order to get from one word to another.  If the edit distance is small, say one character, then someone probably had a typo, and the words are likely the same.  Let's see a way we can check the edit distance in python:

```
import distance
print distance.levenshtein("Hello there","hello there")
```

The result of this computation is a long where a distance of 0, means the two words are the same.  Any other distance will be a positive number.  So if one character is different, the distance between the two strings will be 1, a difference of two characters two, and so on.

###Edit distance and other factors

The next distance we'll look at is Jaro-Winkler.  Like levenshtein's distance metric, Jaro-Winkler looks at the edit distance between two words, however it does things in a more sophisticated way.  Rather than only considering the number of characters you'd need to change in order to get from one string to another, it considers the order of the characters that are the same, the number of spaces you'd need to move those characters so they'd be in the same order, and the number of characters that are different.  For short words, Jaro-Winkler is ideal and will usually outperform levenshtein distance.  However, it won't be best for all possible cases, so its important to be careful.  For instance, in long words, with lots of typos Jaro-Winkler will likely not do very well.  It should be noted that Jaro-Winkler is great for record linkage.

```
import jellyfish
print jellyfish.jaro_winkler(u'Hello there new friends',u'hello there new friend')
```

Notice a few things here - (1) we need to use unicode strings (mildly annoying), (2) jaro-winkler returns a number between 0 and 1 (a float).

###Looking at stemming

Another way of checking if two words are semantically the same is by looking at substrings.

The following code is just an example of how one might go about doing this, a trie is likely a far more compact and interesting way to look at substrings.  It is of my own design (as far as I know), and is extremely simple-minded:

```
def str_comp(str1,str2):
    score = 0
    words1 = str1.split(" ")
    words2 = str2.split(" ")
    if len(words1) < len(words2):
        for ind,word in enumerate(words1):
            score += word_comp(word,words2[ind])
    else:
        for ind,word in enumerate(words2):
            score += word_comp(word,words1[ind])
    return score

def word_comp(str1,str2):
    subword1 = [str1[:pos] for pos in xrange(1,len(str1)+1)]
    subword2 = [str2[:pos] for pos in xrange(1,len(str2)+1)]
    score = 0
    if len(subword1) < len(subword2):
        for ind,sub in enumerate(subword1):
            if sub == subword2[ind]:
                score += 1
        return score/float(len(subword1)*2)
    else:
        for ind,sub in enumerate(subword2):
            if sub == subword1[ind]:
                score += 1
        return score/float(2*len(subword2))
```

While this is clearly not the best possible way to do compare two words based on substring it gets at the point - the more the beginnings of the words are the same the higher the overall score, because if a word has the first five characters in common this will mean the score is greater than if only the first three characters are in common.  However, this assumes that some of the first few characters are in common or the words can't possibly be the same or similar in meaning.  This represents a problem for words that don't come from the same root word, but have similar meanings and therefore it is intended to only illustrate the idea, rather than being rigorous.  

###Looking at Colocation

In the previous sections we looked at the words themselves.  What if two words refer to the same thing but are described with different nouns?  Like perhaps if a person has a nick name.  Looking at the most frequent words around a given word can help us that.  For this analysis we'll make use of something called a n-gram.  The best way to understand an N-gram, is to see it.  

We will use the same sentence through out:

Hi, my name is Eric.  

A 1-gram of that sentence would be:


[('Hi,'), ('my'), ('name'), ('is'), ('Eric.')]


A 2-gram of that sentence would be:

[('Hi,', 'my'), ('my', 'name'), ('name', 'is'), ('is', 'Eric.')]

A 3-gram of that sentence would be:

[('Hi,', 'my', 'name'), ('my', 'name', 'is'), ('name', 'is', 'Eric.')]

As you can see the number in front of gram determines how many elements each split we have.  Also, we only increment the element by one in the sentence.  This creates small phrases, which make up the elements of the n-gram.

Here's the code I used to generate the above sequences:

```
def ngram(sentence,n):
    input_list = [elem for elem in sentence.split(" ") if elem != '']
    return zip(*[input_list[i:] for i in xrange(n)])
```

The zip function will zip n many lists together into one list, where the elements of each list will become tuples. A small piece of syntactic sugar you may not be familiar with is the * in front of the list comprehension.  

To understand the difference here let's look at an example:

```
#basic example
def thing(*x): print x
>>> thing([[elem] for elem in xrange(5)])
([[0], [1], [2], [3], [4]],)
>>> thing(*[[elem] for elem in xrange(5)])
([0], [1], [2], [3], [4])

#with zip
>>> zip([[elem] for elem in xrange(5)])
[([0],), ([1],), ([2],), ([3],), ([4],)]
>>> zip(*[[elem] for elem in xrange(5)])
[(0, 1, 2, 3, 4)]
```

As you can see, the * being passed into a function simply empties the elements of the list comprehension one by one, which is exactly what we want for our zip function.

Using our ngram function we can do the following:

```
def similarity_analysis(doc_one,doc_two):
    ngrams_one = [ngram(doc_one,elem) for elem in xrange(1,4)]
    ngrams_two = [ngram(doc_two,elem) for elem in xrange(1,4)]

    #longer body of text should be looped through
    if len(ngrams_one) < len(ngrams_two):
        ngrams_one,ngrams_two = ngrams_two, ngrams_one
    word_choice_count = 0 
    phrase_choice_count = 0
    for elem in ngrams_one[0]:
        if elem in ngrams_two[0]:
            word_choice_count += 1
    word_choice_similarity = float(word_choice_count)/len(ngrams_one[0])

    phrases_one = ngrams_one[1] + ngrams_one[2]
    phrases_two = ngrams_two[1] + ngrams_two[2]
    for elem in phrases_one:
        if elem in phrases_two:
            phrase_choice_count += 1
    phrase_choice_similarity = float(phrase_choice_count)/len(phrases_one)
    return word_choice_similarity, phrase_choice_similarity
```

Rather than working at the word level checking for similarity, ngrams are good for checking similarity at the document level.  Another document similarity algorithm is Term Frequency Inverse Document Frequency(TFIDF).  Using TfIdf we can determine how important a given word is for a document.  So how does this metric work?  

Simply put the term frequency is the number of times the word appears in a document, divided by the total number of words in that document, and the inverse document frequency is the log of the number of documents in the corpus divided by the number of documents where the specific term appears.

Implementing this is obviously simple for a small amount of text, however as the amount of text grows, its important that our implementation be efficient.  Fortunately sci-kit learn has implemented an efficient implementation of this metric:

```
from sklearn.feature_extraction.text import TfidfVectorizer

def TfIdf(document_list):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(document_list)
    return vectorizer,X

corpus = [
    "Hello there, my name is Eric, will you by my friend?",
    "Hi there, I'm olaf, and I like warm hugs",
    "Oh hey there, my name is billop, and my mother didnt want to name me bill or phillip, so she named me billop",
    "Hello, my name is the rock, and can you smell what I'm cooking?  It's a pie, for your face"]

vectorizer,result = TfIdf(corpus)
print dict(zip(vectorizer.get_feature_names(),vectorizer.idf_))

```

Using this metric we get a nice ranking of the important words across the corpus.  We can use this to determine what are the most important words in the corpus.  And when comparing two corpora, if the words that are ranked highest and lowest are similar, we can guess that the corpora might be the same.  Or at least similar enough that we may believe they are written by the same person.  While it is easy to see how distance metrics can be used to resolve individual words as referring to the same thing, it may be harder to understand the need for resolution at the document level.  If large pieces of texts are very similar, we may believe that the documents are the same and that some words may have merely been mis-spelled.

So here is some code that could be used to do some more sophisticated entity resolution:

```


Here we make use of TfIdf, n-gram analysis, and a few distance metrics.  As you can see, applying the two meta similarity scores and then looking for a cut-off value can save time, although it isn't perfect.  



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

We model our data as sqlalchemy's general purpose Object Relational Model.  The individual fields are modeled via db.Column.  We then inform the database what to do on instantiate of our record object - with the __init__ method.  Notice that we don't need to pass an id, it is generated automatically.  The id is good practice and is useful for indexing data, allowing for faster queries, and database tunning generally.  

Now we can explore the other part of our database class:

```
def __repr__(self):
    return  "<store %r>" % self.name
```

Here we make use of the __repr__ method which will determine the representation of individual objects of our database, assuming we want high level information about the objects.  We can also access individual fields from our objects in the following way:

testing_database.py:

```
from app.server import Store

store = Store.query.all()[0] #get any old object.
print store.name
print store.email
```

Notice that we can access the individual fields, and so, __repr__ is more of a notational convenience more than anything else.  This way we can know what object we are dealing with, without having to deal with accessors.

Now let's look at the controller:

```
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

Here we don't have a ton of new stuff.  Notice that we only expose a `POST` method for our add_route, which will be used for submitting our form data.  Notice that I name the route the same as the method, this is good practice, as we will see, for `url_for`, which resolves method names to their url.

At this point, it makes sense to bring in the html to understand the interaction between the view and the controller:

```
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>

<form method="post" action="{{url_for('add_data')}}">
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

So as you can see, the form action calls the add_data route, via url_for.  Notice the use of openning - `{{` and closing `}}`.  This is what tells the jinga template engine to execute different python and flask methods.  Typically it's for calling routes, rendering data, or resolving urls.  Notice also that the name attribute is present in both of the input fields and these correspond to the `request.form.get`, which grabs the necessary input from the form.  Finally, we can look back at our controller:  

```
store = Store(name,email)
db.session.add(store)
db.session.commit()
```

These three lines are what create our Store object, with our name and email and then save these values to our database.  Notice there was no specific connection made here, nor any database specific code.  Meaning, we can safely swap databases by changing a single line of code: 

`app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"`

The two recommended databases are postgres and sqlite - postgres for production and sqlite for local testing, however SQLAlchemy supports a plethora of datastores.  

Next, let's look at this part of the html:

```
<ul>
{% for datum in data %}
 <li> {{datum.name}} , {{datum.email}} </li>
{% endfor %}
</ul>
```

Here we see a dynamically generated list, that grows with the size of our data list.  Notice that we can access specific data from our datum, since data is a list of type Store.  The `{{ }}` is used to evaluate individual datum.  Notice also that we need an `endfor` statement, ending our for-loop.

This html corresponds to the index method:

```
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html",data=Store.query.all())
```

Notice that data is passed as an optional parameter to the `render_template` function, which is why the list is called data in the html.  Whatever we name the optional parameter, will be the name of that parameter on the front end.  The render_template function accepts all native python data structures - variables, lists, and dictionaries.  In this case, we pass a list, which is all the objects in the Store table.  Notice that we chose to pass all, but we could also have filtered on certain parameters.  To filter a query with sqlalchemy objects we simply need to do something like the following:

`print [obj for obj in Store.query.filter(Store.name == 'Eric')]`

As you can see, the filter expects anything that would satisfy a WHERE clause in SQL.  Most of the time I just work with basic booleans like equality, less than or greater than, but other more complex query terms are possible.  

##C3.js, D3.js and Vincent

We now have all the necessary rigging to work with C3.js or D3.js, vincent, or any other data visualization package we could want.  Let's start with C3.js since it is very easy.

###C3.js and flask

Now that we understand how flask works, we are ready to jump into C3.js!  With C3 we can make beautiful dynamic charts and graphs with just a few lines of code.  There isn't too much new in the server below, since that we are generating random lists of integers to be visualized.  

server.py:

```
from flask import Flask,render_template
import json
from random import randint
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    data1 = ['data1']
    data2 = ['data2']
    for i in xrange(0,randint(0,15)):
        data1.append(randint(0,150))
    for i in xrange(0,randint(2,25)):
        data2.append(randint(7,450))
    return render_template("line_chart.html",data1=json.dumps(data1),data2=json.dumps(data2),data3=json.dumps(data1))


app.run(debug=True)
```

Here is where all the magic happens, specifically within the script tags:

line_chart.html:
```
<html>
	<head>
		<title>Data Viz example</title>

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.10/c3.min.css">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.10/c3.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js"></script>
	</head>
	<body>

	<div id="chart"></div>
 		
	<script>
		var data1 = JSON.parse({{data1|tojson}});
		var data2 = JSON.parse({{data2|tojson}});
		var data3 = JSON.parse({{data3|tojson}});
		var chart = c3.generate({
			bindto: '#chart',
		    data: {
		        columns: [
		            data1,
		            data2
		        ]
		    }
		});
	</script>

</body>
</html> 		
 ```

 Notice that we need to create a div tag with an id that is the same as the bindto parameter in our `c3.generate` function.  In this case we chose to name our id chart.  Notice the use of the `#` infront of chart.  Notice also that we create a variable called chart for this chart that will be generated.  Notice also that adding or data to our graph is extremely easy, we just need to include our columns.  Since the data is being loaded from the server, it might not be clear what these columns of data look like.  So let's be explicit:

 `data1` will be a list, where the first element (at index 0) is the name of the data set, in this case, data1.  This is stored as a string.  The rest of the elements are technically optional and can be an integer or a float.  So data1 might look like this:

 `['data1', 4,17,25,47]`

 The same pattern will hold for data2 and any other columns you may want to add.  

 With c3 we can make lots of types of charts very, very easily!

You can find more examples and the complete server for splines, bar charts, and pie charts in the github [here](https://github.com/EricSchles/book_tools/tree/master/code/chapter3/data_viz).

##Free GIS Systems, in Python

Now that we've learned how to use flask and do some web development, we'll turn out attention to something somewhat different: GeoDjango.  GeoDjango is the Django MVC framework, with added support for Geographic Information Systems.  A GIS system is a visual way of representing data on a physical map.  The most well known example of this is google maps.  With google maps you can embed nearly limitless amounts of data and make that data intuitive, easy to understand and interpret, and also make the data useful.  That's really the goal of all of data science, and certainly the goal of this book.  A good GIS system aims to make data obvious and clear so human connections can be made easily and without any technical ability or understanding.  

So enough chatting about how awesome this stuff is, let's do some of it!  Fortunately Django is one of the most mature and well documented web frameworks around.  So I'll just reference [that documentation](https://docs.djangoproject.com/en/1.8/) so you can get up to speed with Django before moving onto GeoDjango.  Hopefull you went through the example application at this point and are now ready for the magic that is GeoDjango.  

##Installation - GeoDjango

First we'll install Geodjango, which luckily comes with Django1.8.  So I'll you'll need to do really is install django, instructions on how to do that can be found [here](https://docs.djangoproject.com/en/1.8/topics/install/), assuming you want the source or anything else.

But really all you need to do is: `sudo pip install django`

Before we can get started with building we'll need to install PostGIS, steps on how to do that can be found [here](http://www.saintsjd.com/2014/08/13/howto-install-postgis-on-ubuntu-trusty.html)

Next we'll need to install the postgres python module - pyscopg2: `sudo pip install pyscopg2`

Next all we need to do is set up GeoDjango to work with PostGIS, and we are off to the races.

Unfortunately the GeoDjango documentation for the first example is confusion and leaves out a few steps, so first we'll have to correct that:

Please note these directions are for Ubuntu 14.04

Installation:

Python:
`sudo pip install django #make sure you are installing django 1.8` 

`sudo pip install pyscopg2`

PostGres:

`sudo apt-get update`

`sudo apt-get install -y postgresql postgresql-contrib`

Testing postgres install:

`sudo -u postgres createuser -P USER_NAME_HERE`

`sudo -u postgres createdb -O USER_NAME_HERE DATABASE_NAME_HERE`

`psql -h localhost -U USER_NAME_HERE DATABASE_NAME_HERE`

Adding PostGIS support:

`sudo apt-get install -y postgis postgresql-9.3-postgis-2.1`

`sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" DATABASE_NAME_HERE`

changing everything to trusted, rather than requiring authentication - DO THIS FOR LOCAL DEVELOPMENT ONLY!!!

`sudo emacs /etc/postgresql/9.1/main/pg_hba.conf`

Change line:

`local   all             postgres                                peer`

To

`local   all             postgres                                trust`

Then restart postgres:

`sudo service postgresql restart`

Getting started with geodjango:

Now we are ready to get started:

`django-admin startproject geodjango`

`cd geodjango`

`python manage.py startapp world`

Now we'll go into the settings.py file:

`emacs geodjango/settings.py`

and edit the databases connection to look like this:

```
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'geodjango',
         'USER': 'geo',
     }
} 
```

Notice that we haven't created the 'geodjango'-database so we'll do that now:

`sudo -u postgres createuser -P geo`

`sudo -u postgres createdb -O geo geodjango`

`sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" geodjango`

we'll also need to edit the installed aps, in the same file:

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'world'
)
```

Great, now we can save and close that.

Next we'll need some data to visualize:

`mkdir world/data`

`cd world/data`

`wget http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip`

`unzip TM_WORLD_BORDERS-0.3.zip`

`cd ../..`

Now let's inspect our data so we now how our model should look - we should try to be consistent with how the data is annotated for portability and extensibility.  

For this we'll need gdal - `sudo apt-get install libgdal-dev python-gdal gdal-bin # the python library is unnecessary but nice to have :)`

Now we can inspect the annotation in the shapefile of our geospatial data:

`ogrinfo -so world/data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3`

We'll use this output to map to our models.py file:

`emacs world/models.py` and type:

```
from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name
```

We are now ready to run our first migration :)

`python manage.py makemigrations`


`python manage.py sqlmigreate world 0001`


`python manage.py migrate`

Making our first map:

Now that we've done all the setup, we can leverage geodjango immmediately to create an interactive map!

We'll need to make a few small edits to some files, but essetentially, we are done:

open the admin.py file and type the following:

emacs world/admin.py:

```
from django.contrib.gis import admin
from models import WorldBorder

admin.site.register(WorldBorder, admin.GeoModelAdmin)
```

Finally we simply need create our admin credentials:

`python manage.py createsuperuser`
`python manage.py runserver`

Now head over to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

and enter your credentials.  Now you have a GIS system that you can play with, load data into, and get analysis out of!


###Chapter 4
Searching across massive data sets
* facial recognition, facial comparison, and image search - building a cbir - easy
* searching across text in mass - easy
* multithreading applications for faster processing - easy
* using Hadoop and spark for search - easy

##Facial recognition, facial comparison, and image search

An important innovation in the world of computers has been search.  We've more or less figured search out, and for the rest of the world, with databases, this is very useful, but for most folks working in government, things are still stored in a file system.  If you want to do file search efficiently, just use [Solr](http://lucene.apache.org/solr/).

However, after text based documents, the second biggest need for search is images.  There are some standard tools out there, but it's actually worth it to play around with your own solution.  Sometimes you'll need some custom stuff, sometimes you'll need to something special, like my boss asked me to do - image recognition and search off of one picture.  I had to get creative since usually results are not that good for a single picture against other pictures, which are not the same shot.  To be clear my task was this:  

If someone was in a picture, find them in all other pictures they appear in. 

No easy feat.  But I got pretty close.  I ended up settling on two techniques/tools - OpenCVs face comparison algorithms and a wonderful post by the writer of [pyimagesearch](http://www.pyimagesearch.com/).  If you haven't seen it, I recommend checking out that blog, it's full of great posts about computer vision.  

So face comparison searches and compares faces against each other, producing a distance metric, the smaller the distance between two faces, IE the smaller the output, the more likely they are the same person's face.  For pyimagesearch, I made use of their [backgroud comparison post](http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/).  In this post Adrian lays out how to compare the backgrounds of two images - by transforming the pictures into histograms, using a visual bag of words, and then making use of a chi^2 distance, to build an index.  Finally, we search across the index to look for a picture or a similar picture in our set of pictures.  From this we can see if the face and background match for a particular picture - if they do, it's probably the same person.  But each of these metrics own their own is powerful for investigations.  Then we can see who else has been in a the same room, and thus who else knows each other.  We can also see this if we can find multiple people in the same picture.  

One note - we could have used Caffe for the background image search.  The trouble with Caffe is, I find it extremely difficult to install.  Also, I'm not terribly good at C++, which is a major drawback.  The following code is written entirely in python (or wrappers in python).  Caffe does have python wrappers for some of its stuff, and it is a wonderful library if you have the computational power to truly leverage it, but most of the time in government you don't have the ability to install whatever you want and you definitely don't have the computational power to leverage such a tool.

Background compare:

The complete code with data can be found [here](https://github.com/EricSchles/book_tools/tree/master/code/chapter4/cbir)
`index_search.py`:

```
import numpy as np
import cv2
import argparse
import csv
from glob import glob


args = argparse.ArgumentParser()
args.add_argument("-d","--dataset",help="Path to the directory that contains the images to be indexed")
args.add_argument("-i","--index",help="Path to where the computed index will be stored")
args.add_argument("-q","--query",help="Path to the query image")
args.add_argument("-r","--result-path",help="Path to the result path")

args = vars(args.parse_args())

class ColorDescriptor:
    def __init__(self,bins):
        self.bins = bins

    #off_center means that we expect no people in the center of the picture
    #this is the feature construction and processing function
    #cX,cY stand for center X and center Y, aka the middle of the picture
    #off_center creates four quadrants for the picture
    #full_picture checks the full picture and only creates one histogram per picture
    #face_compare creates a segmentation around possible faces, and uses only the face to create a histogram
    def describe(self,image,off_center=False,full_picture=False,face_compare=False):
        image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
        features = []
        (h,w) = image.shape[:2]
        (cX,cY) = (int(w*0.5), int(h*0.5))
        segments = [(0,cX,0,cY),(cX,w,0,cY),(cX,w,cY,h),(0,cX,cY,h)]
        if off_center:
            for (startX,endX,startY,endY) in segments:
                cornerMask = np.zeros(image.shape[:2],dtype="uint8")
                cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
                hist = self.histogram(image,cornerMask)
                features.extend(hist)
        elif full_picture:
            hist = self.histogram(image,None)
            features.extend(hist)
        elif face_compare:
            cascPath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascPath)
            #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                image,
                scaleFactor=1.1,
                minNeighbors=2,
                minSize=(25, 25),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            for (x,y,w,h) in faces:
                cornerMask = np.zeros(image.shape[:2],dtype="uint8") 
                cv2.rectangle(cornerMask, (x,y), (x+w, y+h), 255, -1)
                hist = self.histogram(image,cornerMask)
                features.extend(hist)
        else:
            ellipMask = np.zeros(image.shape[:2],dtype="uint8")
            (axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
            cv2.ellipse(ellipMask, (cX, cY), (axesX,axesY), 0,0,360,255,-1)
            for (startX,endX,startY,endY) in segments:
                cornerMask = np.zeros(image.shape[:2],dtype="uint8")
                cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
                cornerMask = cv2.subtract(cornerMask,ellipMask)
                hist = self.histogram(image,cornerMask)
                features.extend(hist)
        return features
    
    def histogram(self,image,mask):
        hist = cv2.calcHist([image],[0,1,2],mask,self.bins,
        [0, 180, 0, 256, 0, 256])
        hist2 = cv2.normalize(hist,np.zeros(image.shape[:2],dtype="uint8")).flatten()
        return hist2

class Searcher:
    def __init__ (self,indexPath):
        self.indexPath = indexPath
    def search(self, queryFeatures, limit=10):
        results = {}
        with open(self.indexPath) as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    features = [float(x) for x in row[1:] if x!= '']
                    d = self.chi2_distance(features, queryFeatures)
                    results[row[0]] = d
            except IndexError:
                pass
        results = sorted([(v,k) for (k,v) in results.items()])
        return results[:limit]
    def chi2_distance(self,histA,histB, eps = 1e-10):
        d = 0.5 * np.sum([((a-b)**2) / (a+b+eps)
                          for (a,b) in zip(histA,histB)])
        return d

if __name__ == "__main__":
    #i have no idea where these numbers came from.. check - http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
    cd = ColorDescriptor((8,12,3))

    if args["index"] and args["dataset"]:
        with open(args["index"],"w") as output:
            for img_type in [".png",".jpg",".PNG",".JPG",".img",".jpeg",".jif",".jfif",".jp2",".tif",".tiff"]:
                for imagePath in glob(args["dataset"] + "/*" + img_type):
                    imageID = imagePath[imagePath.rfind("/") + 1:]
                    image = cv2.imread(imagePath)
                    features = cd.describe(image)
                    features = [str(f) for f in features]
                    output.write("%s,%s\n" % (imageID, ",".join(features)))
    if args["index"] and args["query"]:
        query = cv2.imread(args["query"])
        features = cd.describe(query)
        searcher = Searcher(args["index"])
        results = searcher.search(features,limit=4)
        
        cv2.imshow("query",query)
        for (score,resultID) in results:
            result = cv2.imread(args["result_path"] + "/" + resultID)
            cv2.imshow("Result",result)
            cv2.waitKey(0)
```         

Rather than explaining all this code, because Adrian explains all of it and extremely well, I'll simply explain how to use it:

`python index_search.py -d [directory of pictures] -i [name of file] #create an index`

`python index_search.py -i [name of index file] -q [path to query picture] -r [path to picture directory] #search for a picture`

A specific example: 
    
`python index_search.py -d pic_db/ -i index.csv` 

`python index_search.py -i index.csv -q person.jpg -r pic_db/`


So here's how the code works:

First let's look at the main method:

```
cd = ColorDescriptor((8,12,3))

if args["index"] and args["dataset"]:
    with open(args["index"],"w") as output:
        for img_type in [".png",".jpg",".PNG",".JPG",".img",".jpeg",".jif",".jfif",".jp2",".tif",".tiff"]:
            for imagePath in glob(args["dataset"] + "/*" + img_type):
                imageID = imagePath[imagePath.rfind("/") + 1:]
                image = cv2.imread(imagePath)
                features = cd.describe(image)
                features = [str(f) for f in features]
                output.write("%s,%s\n" % (imageID, ",".join(features)))
if args["index"] and args["query"]:
    query = cv2.imread(args["query"])
    features = cd.describe(query)
    searcher = Searcher(args["index"])
    results = searcher.search(features,limit=4)
    
    cv2.imshow("query",query)
    for (score,resultID) in results:
        result = cv2.imread(args["result_path"] + "/" + resultID)
        cv2.imshow("Result",result)
        cv2.waitKey(0)
```

As you can see there isn't a ton going on here, we loop through all the images in the pictures folder, doing the feature transformations on each picture and then generating an index with all the feature-histogram-vectors.  Now let's dig a little deeper into the describe method.  The describe method acts on the matrix representation of an image.  The image is a matrix at this point, because it was read in with open cv's imread method.  So really the describe method is a matrix transformation, which produces features according to some rules about the image.  The way in which you decide to describe images, turns out to be very very important.  Essentially the describe is doing a segmentation and then a transformation.

One fun thing I did was, I allowed you to segment pictures by face, into four corners, or the way Adrian does it; with four corners and an elliptical in the center.  My ways don't always yield good results, and in fact more than half the time Adrians method works the best, but sometimes, my methods have been effective so I will mention them here.

To understand that we'll look at the segmentation methods one at a time:

```
for (startX,endX,startY,endY) in segments:
    cornerMask = np.zeros(image.shape[:2],dtype="uint8")
    cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
    hist = self.histogram(image,cornerMask)
    features.extend(hist)
```

Here we setup a cornerMask which is a matrix of zeroes.  Notice that we apply the rectangle method, which takes in starting and finishing coordinates and then 'draws' a rectangle on the cornerMask.  Then we create a histogram with the segmentation of the image defined by the rectangle we 'drew' which acts as sort of a boundary.  Depending on how you draw your segmentation, will effect your histogram and thus your features.  

The full picture is uninteresting, because it is just the histogram transformation with no segmentation.  

The next interesting segmentation is one done with semantic meaning built in - finding the startX,startY and endX,endY from the faces in the picture:

```
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    image,
    scaleFactor=1.1,
    minNeighbors=2,
    minSize=(25, 25),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

for (x,y,w,h) in faces:
    cornerMask = np.zeros(image.shape[:2],dtype="uint8") 
    cv2.rectangle(cornerMask, (x,y), (x+w, y+h), 255, -1)
    hist = self.histogram(image,cornerMask)
    features.extend(hist)
```

Here we use opencv's face detection classifier to find all the 'boxes' around the potential faces in the image.  This is then used to create our rectangles, simiarly to the previous example.  However, now rather than segmenting on corners, we segment on faces.  We then use this segmentation to create histograms and finally feature vectors of just the faces.  Unfortunately, in practice this technique tends to perform the worst, for now.  I need to figure out how to better tune my parameters so that this is reliable, or I may abandon it as an idea.  But still, it was fun to try!

The final method is what Adrian did:

```
ellipMask = np.zeros(image.shape[:2],dtype="uint8")
(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
cv2.ellipse(ellipMask, (cX, cY), (axesX,axesY), 0,0,360,255,-1)
for (startX,endX,startY,endY) in segments:
    cornerMask = np.zeros(image.shape[:2],dtype="uint8")
    cv2.rectangle(cornerMask,(startX,startY),(endX,endY),255,-1)
    cornerMask = cv2.subtract(cornerMask,ellipMask)
    hist = self.histogram(image,cornerMask)
    features.extend(hist)
```

Creating an elliptical mask for the center of the picture and generating segments for the remaining four corners and then subtracting the center from the four corners.  Nothing else is new here and thus it can largely be ignored.

The next important piece of the main function is performing a query which is captured here:

```
query = cv2.imread(args["query"])
features = cd.describe(query)
searcher = Searcher(args["index"])
results = searcher.search(features,limit=4)
```

Notice that we describe the query image the same way we described the index.  This is imperative - if we describe our feature vectors differently in indexing and querying, our queries won't work.  

The search function is fairly simple:

```
results = {}
with open(self.indexPath) as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            features = [float(x) for x in row[1:] if x!= '']
            d = self.chi2_distance(features, queryFeatures)
            results[row[0]] = d
    except IndexError:
        pass
results = sorted([(v,k) for (k,v) in results.items()])
return results[:limit]
```

Essentially, it applies the chi^2 distance function to each of the features in the index against the query image's features.  The results are returned in sorted order, lowest to highest.  This is because if the distance is smallest, they are the images can be expected to be the least different.  


###Understanding Face Comparison, With OpenCV

The `face_compare2.py` contains how I do face comparison with open CV.  It works quiet well, but I do confess it is not my most well organized piece of code.  I have not yet learned how to be elegant with image manipulation, alas, the struggles of perfection in a sea of desires and things one aspires to be perfect at.  But such is the calamity of curious minds, and it is something I am proud of, to be pulled in so many possible directions.

Note: For this code to work from this repo, you'll need to install OpenCV from the follow githubs: [opencv](https://github.com/Itseez/opencv), [opencv-contrib](https://github.com/Itseez/opencv_contrib), and it's not a bad idea to install [opencv-extra](https://github.com/Itseez/opencv_extra), but only if you have space for the extra data, it's not necessary.

And the code that I'll reference throughout this section can be found [here](https://github.com/EricSchles/book_tools/tree/master/code/chapter4/face_comparison)

In any event, there is a lot to unpack in that file and so I'm simply going to explain some high level steps:

First we instantiate our recognizers:
```
recog = {}
recog["eigen"] = cv2.face.createEigenFaceRecognizer()
recog["fisher"] = cv2.face.createFisherFaceRecognizer()
recog["lbph"] = cv2.face.createLBPHFaceRecognizer()
```

Notice that recently OpenCV has changed and now the face recognizers live in a seperate supplemental library.  The core of OpenCV can be found here: https://github.com/Itseez/opencv and the face recognizers can be found here: https://github.com/Itseez/opencv_contrib.  I'm not sure why they decided to move such a handy set of tools out into some contrib repo, but that is how it is.

The next thing to do is normalize the pictures:

normalize_cv(filename,compare,directory_of_pictures)

In this case, this means making them all the same height and width, because the face comparison algorithms require this.  I'm not sure why this is the case.  

Next we read in a picture and hand label it 1:

```
face = cv2.imread(new_filename,0)
face,label = face[:, :], 1
```

And we read in a different picture with a different face and hand label it 2:

```
compare_face = cv2.imread(new_compare, 0)
compare_face, compare_label = compare_face[:,:], 2
```

This establishes the base comparison for what will be considered a face we are searching for and a face that is different from the one we want.  Perhaps using 2 isn't the best, because the distance isn't great enough, but this is intended to be a toy example, you should feel free to tune these "magic" numbers to improve the precision of your own code.  

Next we train the each recognizer on the training data:

```
for recognizer in recog.keys():
    recog[recognizer].train(image_array,label_array)
```

And then we compare all the trained data against the directory of pictures:

```
test_images = [(np.asarray(cv2.imread(img,0)[:,:]),img) for img in test_images]
possible_matches = []
for t_face,name in test_images:
    t_labels = []
    for recognizer in recog.keys():
        try:
            [label, confidence] = recog[recognizer].predict(t_face)
            possible_matches.append({"name":name,"confidence":confidence,"recognizer":recognizer})
```

Notice that we simply need to call the predict function on each image in our directory.

Finally, we simply can print out all the possible matches:

```
for i in possible_matches:
	print i
```

Running this code is fairly simple and can be accomplished with the following:

`python face_compare2.py [first picture] [baseline comparison picture] [directory of pictures to search against]`


##Multithreading applications

While Python has a Global Interpretter Lock (GIL), meaning it cannot be truly multithreaded, there are a lot of things you can still do that look and feel like multithreading.  And you can absolutely parallelize your code.  For more on the GIL check out these sources:

* [PythonWiki](https://wiki.python.org/moin/GlobalInterpreterLock)

* [These awesome slides from David Beazley](http://www.dabeaz.com/python/UnderstandingGIL.pdf)

* [This sweet general purpose wikipedia article on GILs](https://en.wikipedia.org/wiki/Global_Interpreter_Lock)

If you are new to doing multiple things in one program, I'll just give you the two second crash course.  Feel free to skip ahead if this is review.

###What's all this then?

When you multithread an application the general idea is that you'll have multiple threads executing different parts of your code independent of one another, but that all of these independent threads will at some point depend on each other again.  This is known as blocking code, because threads cannot continue until other threads complete.  So let's look at a very dumb and simple example.  

Note:  Two of the following examples come from [this great stackoverflow thread](http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies) - summing.py and scraping.py

summing.py:
```
import threading

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i


thread1 = SummingThread(0,500000)
thread2 = SummingThread(500000,1000000)
thread1.start() # This actually causes the thread to run
thread2.start()
thread1.join()  # This waits until the thread has completed
thread2.join()  
# At this point, both threads have completed
result = thread1.total + thread2.total
print result
```

In this example we create multiple threads to sum different pieces of the numbers 0 to 1000000.  Notice that in this example the code cannot move onto the result until both threads 1 and 2 complete their sums over the total range.  This example shows us one way of creating threads and making use of them to get stuff differently.  Now let's compare this with the sequential running example.

summing_time_test.py
```
import threading
from time import time

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i

def summing():
    thread1 = SummingThread(0,500000)
    thread2 = SummingThread(500000,1000000)
    thread1.start() # This actually causes the thread to run
    thread2.start()
    thread1.join()  # This waits until the thread has completed
    thread2.join()  
    # At this point, both threads have completed
    return thread1.total + thread2.total

def regular_sum():
    summa = 0
    for i in xrange(1000000):
        summa += i
    return summa

summing_start = time()
summing()
print "Summing Total Time:", time()-summing_start

regular_sum_start = time()
regular_sum()
print "Regular Total Time:", time() - regular_sum_start
```

You can find this code [here](https://github.com/EricSchles/book_tools/blob/master/code/chapter4/making_code_faster/summing_time_test.py) and experiment yourself :)

As you'll see, if you try this code, the sequential solution actually performs an order of magnititude faster, every time.  So why would you ever do this?  Well, we looked at sort of a toy example to understand how blocking could happen.  It's important to note that in this example every single input ran in the same amount of time, a bad candidate for mutlithreading.  If there are some inputs where computation takes significantly longer, than there will be a vast speed up from doing things out of order.  Specifically, processing the quickly evalutated inputs at the same time as the ones that will take longer.  Of course, tuning this can be tricky because you may not always know what will be a problem until your code is already running.  Of course, we can always create a situation where we know certain inputs will be computationally more intensive then others.  The classical choice for this is computing the fibonacci numbers recursively.  

```
import threading
from time import time

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=fib(i)

def summing():
    thread1 = SummingThread(0,15)
    thread2 = SummingThread(15,30)
    thread1.start() # This actually causes the thread to run
    thread2.start()
    thread1.join()  # This waits until the thread has completed
    thread2.join() 
    # At this point, both threads have completed
    return thread1.total + thread2.total

def regular_sum():
    summa = 0
    for i in range(30):
        summa += fib(i)
    return summa

summing_start = time()
summing()
print "Summing Total Time:", time()-summing_start

regular_sum_start = time()
regular_sum()
print "Regular Total Time:", time() - regular_sum_start
```

Result when taking the sum for the first 30 fibonacci numbers:

Summing Total Time: 1.10466504097
Regular Total Time: 1.83267211914

As you can see there is a slight improvement when using threading over iteration here.  As you may have guessed this improvement increases with two threads as n get's bigger.  Feel free to try some experiments on your own to verify this.  It's important to note that the above result will not be exactly the same, even when you try running the above code.  The only guarantee is that threading will necessarily run faster than just straight iteration.  

Now let's look at a slightly more practical example:

scraping.py:

```
import Queue
import threading
import urllib2

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

theurls = ["http://google.com", "http://yahoo.com"]

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

s = q.get()
print s
```

This is an example of some code that is not blocking.  This means threads can execute simultaneously and don't have to wait for each other to move onto other tasks.  Notice the use of a queue here, which allows us to store our results in one structure, without knowing (or caring) what order they entered the queue.  The reason this is powerful, is let's say we need to scrape a website many times or we need to scrape a bunch of websites at the same time and join some data from all of them together (a task one needs to do often in the anti-human trafficking world), this will be much, much faster with threading, because you can process requests independently of each other.  If you had to wait for each website to scraped before moving onto the next, it would invariably take much, much longer.  

Now let's look at yet another way mutlithreading can be used:

installer.py:

```
from subprocess import call
from multiprocessing import Process
import argparse

def install(requirement,how_to_install,args):
    if args["left_split"]:
        requirement = requirement.split(args["left_split"])[0]
    elif args["right_split"]:
        requirement = requirement.split(args["right_split"])[1]
    if 'sudo' in how_to_install:
        how_to_install = how_to_install.replace("[PACKAGE]",requirement).split(" ")
    else:
        how_to_install = ["sudo"] + how_to_install.replace("[PACKAGE]",requirement).split(" ")
    call(how_to_install)

args = argparse.ArgumentParser()
args.add_argument("-ls","--left-split",help="the package name is to the left of the character or characters to split on")
args.add_argument("-rs","--right-split",help="the package name is to the right of the character or characters to split on")

args = vars(args.parse_args())

with open("requirements.txt","r") as f:
    dependencies = f.read().split("\n")
    dependencies = [dep for dep in dependencies if dep != '']
with open("how_to_install.txt","r") as f:
    how_to_install = f.read().strip()

for dep in dependencies:
    p = Process(target=install,args=(dep,how_to_install,args,))
    p.run()
```

The above code can be found [here](https://github.com/EricSchles/book_tools/tree/master/code/chapter4/installer).

This application is slightly more involved than the previous ones but the idea should be clear enough.  We typically install things sequentially, this application allows us to install requirements in parallel.  Notice here we make use of the `Process` object instead of the threading interface.  The `Process` object is merely a notational convienence and works the same way as threading.Thread but is much easier to write down and doesn't require any business with classes, which is kind of wonderful :).  You can pass in a queue with a `Process` object very easily as the following simple example shows:

```
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print q.get()    # prints "[42, None, 'hello']"
    p.join()
```

This example was lifted directly from the [mutliprocessing docs](https://docs.python.org/2/library/multiprocessing.html).

As you can see, we simply pass in a queue to the target function and pass in the results, rather than doing a return statement.  