import pandas as pd
from hackthederivative import complex_step_finite_diff as derivative
#https://pygotham.org/2015/talks/115/hack-the-derivative/

def frange(start,end,step=0.1):
    listing = [start]
    cur = start
    while cur < end:
        cur += step
        listing.append(cur)
    return listing

#(x-5)^2 - 3.5*(x-5) + 8
def calc_hours(volunteers):
    return (volunteers-5)**2 - 3.5*(volunteers - 5) + 8

df = pd.DataFrame()

for i in frange(0,10.0):
    tmp = {}
    tmp["value"] = i
    tmp["derivative"] = derivative(calc_hours,i)
    df = df.append(tmp,ignore_index=True)
df.to_csv("result.csv")

