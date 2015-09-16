import pandas as pd
import shapefile
# http://www.digital-geography.com/importing-shapefiles-in-python/#.VfBKBXUViko
from glob import glob
from shapely.geometry import Point, MultiPoint 
#check out http://streamhacker.com/2010/03/23/python-point-in-polygon-shapely/, http://toblerity.org/shapely/manual.html#points
from unidecode import unidecode
import time
import random
from multiprocessing import Process,Queue
#where I got the data: http://www.zillow.com/howto/api/neighborhood-boundaries.htm

#This method transforms the shape file from zillow and finds all the points for the 
#different neighborhoods around the city
#This can easily be extended to find any neighborhood in the zillow dataset
#This method returns a list of geo objects which come from the shapefile object, check out pyshp for more info!
def grab_nyc_neighborhoods():
    filename = glob("*.shp")
    ctr = shapefile.Reader(filename[0])
    geomet = ctr.shapeRecords()
    nyc = []
    for geo in geomet:
        if any([place for place in geo.record if type(place) == type(str()) and "New York City" in place]):
           nyc.append(geo)
    return nyc

#This method determines whether or not a give point is inside a neighborhood by looping through all the neighborhoods
#and then just stating whether or not it's in the neighborhood or not
#neighborhoods is a list of geo objects which come from the shapefile object - check out pyshp for more info
def determine_neighborhood(nyc,location):
    point = Point((location["lat"],location["long"]))
    neighborhoods = []
    for geo in nyc:
        points = [tuple([ind_point[1],ind_point[0]]) for ind_point in geo.shape.points]
        poly = MultiPoint(points).convex_hull
        if point.within(poly):
            neighborhoods.append(geo)
    return neighborhoods

#This method is the main workhorse of the program
#It figures out what neighborhood each point is in
#It then passes back a dataframe which will be saved when all pieces of information are processed
def create_neighborhood_grouping(nyc,location,q):
    tmp_dict = {}
    neighborhood = determine_neighborhood(nyc,location)
    if len(neighborhood) >= 1:
        neighborhood = neighborhood[0]
        tmp_dict["neighborhood"] = neighborhood.record
    else:
        tmp_dict["neighborhood"] = ""
    tmp_dict.update(location)
    q.put(tmp_dict)

#This method processes the csv
def process_csv(doc):
    df = pd.DataFrame().from_csv(doc,index_col=False)
    locations = []
    for i in df.index:
        locations.append({"lat":df.ix[i]["Latitude"], "long":df.ix[i]["Longitude"],})
    return locations

#As you can see here we have a main -> 
#The main gets the locations, saves them to a dataframe and then saves that dataframe to a csv
if __name__ == '__main__':
    nyc = grab_nyc_neighborhoods()
    print "getting lat/long"
    locations = process_csv("random_lat_long.csv")
    df = pd.DataFrame()
    print "creating dataframe"
    results = []
    q = Queue()
    for ind,loc in enumerate(locations):
        print loc, ind
        p = Process(target=create_neighborhood_grouping,args=(nyc,loc,q))
        p.start()
        results.append(q.get())
    for result in results:
        df = df.append(result,ignore_index=True)
    df.to_csv("grouping.csv")
    
