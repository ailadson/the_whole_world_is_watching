import json
from google.appengine.api import urlfetch

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