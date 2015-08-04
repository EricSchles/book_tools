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

Note - add source code here from work, but take out anything important.  

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

Rather than working at the word level checking for similarity, ngrams are typically used for checking similarity at the document level.  Another document similarity level 

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

[angular.js]()





