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

