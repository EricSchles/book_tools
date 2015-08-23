from differ import Diff
from email_server import Emailer
from datetime import date,timedelta
from glob import glob
import os
import json

class Alert:
    def __init__(self):
        self.sites = self.parse_sites()
        self.emailer = Emailer()
    def parse_sites(self):
        websites = json.load(open("websites.json","r"))
        sites = []
        for website in websites:
            sites.append(website.split(".")[1])
        return sites

    def alert(self):
        for site in self.sites:
            self.send_alert(site)
        
    def send_alert(self,site):
        record_sets = glob("../storage/"+site+"*")
        today = str(date.today()).replace("-","")
        yesterday = str(date.today() - timedelta(days=1)).replace("-","")
        todays = []
        yesterdays = []
        diff = Diff()
        for record_set in record_sets:
            if today in record_set:
                todays.append(record_set)
            if yesterday in record_set:
                yesterdays.append(record_set)

        today_hashes = []
        for today in todays:
            os.chdir(today)
            with open("sha_hashes.txt","r") as f:
                today_hashes.append(f.read().split("\n"))
            os.chdir("../")

        yesterday_hashes = []
        for yesterday in yesterdays:
            os.chdir(yesterday)
            with open("sha_hashes.txt","r") as f:
                yesterday_hashes.append(f.read().split("\n"))
            os.chdir("../")

        #any variable with _t is today
        #any variable with _y is yesterday
        for hash_set_t in today_hashes:
            for ind_t,hashing_t in enumerate(hash_set_t):
                name_t = hashing_t.split("000")[1].split(":")[0]
                hash_val_t = hashing_t.split(":")[1]
                for hash_set_y in yesterday_hashes:
                    for ind_y,hashing_y in enumerate(hash_set_y):
                        hash_val_y = hashing_y.split(":")[1]
                        if name_t in hashing_y:
                            if hash_val_t != hash_val_y:
                                self.emailer.add_website(site)
                                self.emailer.add_message("the website was updated")
                                self.emailer.send()

if __name__ == '__main__':
    alerter = Alert()
    alerter.alert()
