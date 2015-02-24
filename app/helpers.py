from google.appengine.api import urlfetch
import json
import uuid
import datetime
import dateutil.parser
from datastore import Record
from google.appengine.ext import db


def createLocData(postData):
    locData = {}
    lat = postData("lat")
    lng = postData("lng")
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lng
    jData = urlfetch.fetch(url=url,follow_redirects = False).content
    data = json.loads(jData)
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
            
    return locData

#--------------------------------------

def createRecord(postData,locationData,filename,type):
    vidRecord = Record(id=str(uuid.uuid4().int))
    
    vidRecord.created = datetime.datetime.today()
    #TO DO vidRecord.user
    print(dateutil.parser.parse(postData("date")).date())
    vidRecord.date = dateutil.parser.parse(postData("date")).date()
    if postData("firstName"):
        vidRecord.firstName = postData("firstName") 
    if postData("lastName"):
        vidRecord.lastName = postData("lastName") 
    if postData("race"):
        vidRecord.ethnicity = postData("ethnicity")
    if postData("ability") == 'on':
        vidRecord.ability = True       
    if postData("age"):
        vidRecord.age = int(postData("age"))   
    if postData("gender"):
        vidRecord.gender = postData("gender")
    if postData("oFirstName"):
        vidRecord.oFirstName = postData("oFirstName")
    if postData("oLastName"):
        vidRecordoLastName = postData("oLastName")
    if postData("oRace"):
        vidRecord.oRace = postData("oRace") 
    if postData("dept"):
        vidRecord.dept = postData("dept")
    if postData("badge"):
        vidRecord.badge = postData("badge")
    if postData("about"):
        vidRecord.about = db.Text(arg=postData("about"))
    vidRecord.lat = float(postData("lat"))
    vidRecord.lng = float(postData("lng"))
    if "country" in locationData:
        vidRecord.country = locationData["country"]
    if "state" in locationData:
        vidRecord.state = locationData["state"]
    if "city" in locationData:
        vidRecord.city = locationData["city"]
    if "neighborhood" in locationData:
        vidRecord.neighborhood = locationData["neighborhood"]
    if "city_state" in locationData:
        vidRecord.city_state = locationData["city_state"]
    if "zipCode" in locationData:
        print(locationData["zipCode"])
        vidRecord.zipCode = locationData["zipCode"]
    if postData("type") == 'brutal' :
        vidRecord.brutal = True;
    elif postData("type") == 'fatal' :
        vidRecord.fatal = True;
    elif postData("type") == 'wrongful' :
        vidRecord.wrongful = True;
    elif postData("type") == 'interaction' :
        vidRecord.interaction = True;    
    vidRecord.promoted = 0
    vidRecord.raw = filename
    vidRecord.put()