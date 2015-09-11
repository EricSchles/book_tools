# Data to generate:
# * What percentage of people openned emails?
# 	* What time of day was the email openned?  
# 	* What was the subject line?  
# 		* Was a formal or casual subject line used?
# 		* Was the person's name used in the subject line?  
# 			* First name or last name used?
# 	* What was the email address that sent the email?

import random
import pandas as pd

df = pd.DataFrame()
for i in xrange(100):
    record = {}
    #What percentage of people openned emails
    record["open_rate"] = random.random() + 0.15
    if record["open_rate"] > 1.0:
        record["open_rate"] = 1.0
        
    #What time of day was the email openned?
    #{"morning":1,"midday":2,"evening":3}
    record["time_of_day"] = random.randint(1,3)
    
    #What was the subject line?
    #{"Hello there!":1,"Oh hi":2}
    record["subject_line"] = random.randint(1,2)
    
    #Was a formal or casual subject line used?
    #{"formal":1,"casual":2}
    record["formal_casual_subject"] = random.randint(1,2) 
    
    #Was the person's name used in the subject line?
    #{"persons name":1,"no name present":2}
    record["name_present"] = random.randint(1,2)
    
    #First name or last name used?
    #{"first_name":1,"last_name":2}
    record["first_last_name"] = random.randint(1,2)
    
    #What was the email address that sent the email?
    #{"hello@non_profit.org":1,"ericschles@non_profit.org":2}
    record["email_address"] = random.randint(1,2)
    df = df.append(record,ignore_index=True)

df.to_csv("marketing_data.csv")

