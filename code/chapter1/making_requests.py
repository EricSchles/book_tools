import requests
from multiprocessing import Process

#Text
intro = """
The requests library is extremely powerful and very high level.  It can be used to do a whole bunch of things!

To fully understand it's power, check out the docs:

http://docs.python-requests.org/en/latest/
"""

methods1 = """
Requests gives you a ton of power, check out all the methods that come with the request object."""

methods2 = """
The some of the most important parts of the request object are:

1) text
2) url
3) content
4) raw
5) headers
"""

signin1 = """
In addition to being able to get certain information back from a request, we can add optional parameters to the request.  The auth parameter is typically used for authenticating to an api and will send along credentials in a tuple.  This is extremely useful for testing if your login page can be brute forced, as well as, making api requests for you :)"""

signin2 = """
You can also send data to a server after a page has loaded, for that we'll need the data parameter, which expects a dictionary.
"""

signin3 = """
Perhaps the most useful method is the send file, allowing you to pass files across a connection.  This especially useful for applying to jobs ;) but also has a great use case in the government.  """


#Functions
def method_list():
    r = requests.get("https://www.google.com")
    for method in dir(r):
        if not "_" in method:
            print method
    
def sign_in():
    data = ('admin','1234')
    print
    print 
    print "making request: requests.get('http://localhost:5000/secret-page',auth=data)"
    print 
    r = requests.get("http://localhost:5000/secret-page",auth=data)
    if r.text == "success":
        print "successfully logged onto the server"
    
def form_fill():
    payload = {"username":"eric","pass":"1234"}
    print
    print "making request: requests.post('http://localhost:5000/form',data=payload)"
    print 
    r = requests.post("http://localhost:5000/form",data=payload)
    if r.text == "success":
        print "successfully filled out a form!"

def send_file():
    files = {"file": open("report.csv","r")}
    print
    print "making request: requests.post('http://localhost:5000/get_csv',files=files)"
    print 
    r = requests.post("http://localhost:5000/get_csv",files=files)
    if r.text == "success":
        print "successfully uploaded a file"
    
def shutdown():
    p = requests.post("http://localhost:5000/shutdown")
    print p.text
    print

print intro
print methods1
method_list()
print methods2
print signin1
try:
    sign_in()
    print signin2
    form_fill()
    send_file()
    shutdown()
except:
    print "Please start the server in order for the sign_in example to run"
    print "do this by typing python test_auth_server.py in the chapter 1 directory (from the command line)"
