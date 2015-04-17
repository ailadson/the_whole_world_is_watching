from google.appengine.api import urlfetch
import json
import uuid
import mimetypes
import os
import datetime
import dateutil.parser
import cloudstorage as gcs
from datastore import Record
from google.appengine.ext import db
from google.appengine.api import app_identity


def createLocData(lat,lng):
    locData = {}
    locData["lat"] = float(lat)
    locData["lng"] = float(lng)
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lng
    jsonData = urlfetch.fetch(url=url,follow_redirects = False).content
    data = json.loads(jsonData)
    components = data['results'][0]['address_components']
    check = {
        "neighborhood":"neighborhood",
        "administrative_area_level_1":"state",
        "administrative_area_level_2":"city_state",
        "locality":"city",
        "country":"country",
        "postal_code":"zipCode"
    }
    
    for component in components:
        if component['types'][0] in check:
            locData[check[component['types'][0]]] = component['long_name']
            
    for key in check.values():
        if key in locData.keys(): pass
        else:
            locData[key] = ""
            
    return locData

#--------------------------------------
def createGCSObject(f, name):
    my_default_retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=15)
    gcs.set_default_retry_params(my_default_retry_params)
    
    
    filename = '/net_wwwatching/'+name
    file = gcs.open(filename,mode='w',options={'x-goog-acl':'public-read'})
    file.write(f)
    file.close()

def createRecord(postData,locationData,f):
    
    r = Record() #create record
    r.id = str(uuid.uuid4().int)
    r.created = datetime.datetime.today()
    
    #location data
    r.lat = locationData["lat"]
    r.lng = locationData["lng"]
    r.country = locationData["country"]
    r.state = locationData["state"]
    r.city = locationData["city"]
    r.neighborhood = locationData["neighborhood"]
    r.city_state = locationData["city_state"]
    r.zipCode = locationData["zipCode"]
    
#    r.user = "not implemented"
    r.date = dateutil.parser.parse(postData("date")).date()
    
    if postData("firstName"): r.firstName = postData("firstName") 
    if postData("lastName"): r.lastName = postData("lastName") 
    if postData("race"): r.ethnicity = postData("ethnicity")
    if postData("ability") == 'on': r.ability = True #change      
    if postData("age"): r.age = int(postData("age"))   
    if postData("gender"): r.gender = postData("gender")
    if postData("charged") == 'on': r.charged = True
    if postData("chargedWith"): r.chargedWith = postData("chargedWith")
    if postData("convicted") == 'on': r.convicted = True
        
    if postData("oFirstName"): r.oFirstName = postData("oFirstName")
    if postData("oLastName"): r.oLastName = postData("oLastName")
    if postData("oRace"): r.oRace = postData("oRace") 
    if postData("dept"): r.dept = postData("dept")
    if postData("badge"): r.badge = postData("badge")
        
    if postData("about"): r.about = db.Text(arg=postData("about"))
    if postData("type") == 'brutal' :
        r.brutal = True;
    elif postData("type") == 'fatal' :
        r.fatal = True;
    elif postData("type") == 'wrongful' :
        r.wrongful = True;
    elif postData("type") == 'interaction' :
        r.interaction = True;
        
    r.views = 0
    r.promoted = 0
    r.encoded = False;
    r.flagged = True;
    r.flagReason = "NEW"
    r.put()
    
    #create raw
    createGCSObject(f, r.id+".raw")
    
    return r