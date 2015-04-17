from google.appengine.ext import db

class Record(db.Model):
    #required standard7
    #required location
    lat = db.FloatProperty()
    lng = db.FloatProperty()
    country = db.StringProperty()
    state = db.StringProperty()
    city_state = db.StringProperty()
    city = db.StringProperty()
    neighborhood = db.StringProperty()
    zipCode = db.StringProperty()
    
    #REST OPTIONAL
    #standard data
    user = db.UserProperty()
    date = db.DateProperty()
    
    #arrested data
    firstName = db.StringProperty()
    lastName = db.StringProperty()
    ethnicity = db.StringProperty()
    gender = db.StringProperty()
    age = db.IntegerProperty()
    ability = db.BooleanProperty()
    charged = db.BooleanProperty()
    chargedWith = db.StringProperty()
    convicted = db.BooleanProperty()
    
    #officer data
    oFirstName = db.StringProperty()
    oLastName = db.StringProperty()
    badge = db.StringProperty()
    oRace = db.StringProperty()
    dept = db.StringProperty()
    oCharged = db.BooleanProperty()
    oChargedWith = db.StringProperty()
    oConvicted = db.BooleanProperty()
    
    #incident data
    about = db.TextProperty()
    brutal = db.BooleanProperty()
    fatal = db.BooleanProperty()
    wrongful = db.BooleanProperty()
    interaction = db.BooleanProperty()
    
    #meta data
    promoted = db.IntegerProperty()
    encoded = db.BooleanProperty()
    views = db.IntegerProperty()
    flagged = db.BooleanProperty()
    flagReason = db.StringProperty()
    

#--------------------------------------------------#

class ModerateRecord(db.Model):
    #required standard
    id = db.StringProperty(required=True)
    approved = db.BooleanProperty()
    flagReason = db.StringProperty()
    approvedBy = db.StringListProperty()
    rejectedBy = db.StringListProperty()
    data = db.TextProperty()
    
    
    
    
    