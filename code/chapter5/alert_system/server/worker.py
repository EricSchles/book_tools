from sys import argv
import pickle
import os
import time
import differ
from alerts import Alert

def wrapper(map_obj,website,depth,listing):
    
    while True:
        print "started mapper.."
        links = map_obj.mapper(website,depth,listing)
        print "Started storing links for the above website"
        cur_dir = os.getcwd()
        os.chdir("../storage")
        map_obj.storing(links)
        print "finished storing links"
        os.chdir(cur_dir)
        alerter = Alert()
        alerter.alert()
        time.sleep(86400)

        
if __name__ == '__main__':
    m = pickle.loads(argv[1])
    website=argv[2]
    depth= int(argv[3])
    listing=pickle.loads(argv[4])
    wrapper(m,website,depth,listing)
