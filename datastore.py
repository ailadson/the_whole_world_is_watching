from google.appengine.ext import ndb

class Record(ndb.Model):
    #required location
    lat = ndb.FloatProperty()
    lng = ndb.FloatProperty()
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city_state = ndb.StringProperty()
    city = ndb.StringProperty()
    neighborhood = ndb.StringProperty()
    zipCode = ndb.StringProperty()

    #upload data
    user_ip = ndb.StringProperty()
    user_email = ndb.StringProperty()
    date = ndb.DateProperty(auto_now_add=True)
    cloud_url = ndb.StringProperty()

    #arrested data
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    race = ndb.StringProperty()
    gender = ndb.StringProperty()
    age = ndb.IntegerProperty()
    ability = ndb.BooleanProperty()
    charged = ndb.BooleanProperty()
    chargedWith = ndb.StringProperty()
    convicted = ndb.BooleanProperty()

    #officer data
    officerFirstName = ndb.StringProperty()
    officerLastName = ndb.StringProperty()
    officerBadge = ndb.StringProperty()
    officerRace = ndb.StringProperty()
    officerGender = ndb.StringProperty()
    officerDept = ndb.StringProperty()
    officerCharged = ndb.BooleanProperty()
    officerChargedWith = ndb.StringProperty()
    officerConvicted = ndb.BooleanProperty()

    #incident data
    about = ndb.TextProperty(indexed=False)
    brutal = ndb.BooleanProperty()
    fatal = ndb.BooleanProperty()
    docile = ndb.BooleanProperty()

    #meta data
    promoted = ndb.IntegerProperty()
    encoded = ndb.BooleanProperty()
    views = ndb.IntegerProperty()
    flagged = ndb.BooleanProperty()
    flagReason = ndb.StringProperty()
