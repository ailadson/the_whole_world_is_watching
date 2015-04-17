import uuid
from createGCSObject import createGCSObject

def createRecord(postData,locationData,f,type):
    
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
    vidRecord.raw = vidRecord.id+'.raw'
    vidRecord.put()
    #create raw
    createGCSObject(f,"raw/"+vidRecord.id+".raw");