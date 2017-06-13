from google.appengine.ext import ndb

class IncidentEntity(ndb.Model):
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
    upload_ip = ndb.StringProperty(required=True)
    user_email = ndb.StringProperty()
    date = ndb.DateProperty(auto_now_add=True)
    cloud_id = ndb.StringProperty(required=True)

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

    #stage
    has_encoded_files = ndb.BooleanProperty(default=False)
    has_required_data = ndb.BooleanProperty(default=False)
    has_optional_data = ndb.BooleanProperty(default=False)

    #meta data
    promoted = ndb.IntegerProperty(default=0)
    views = ndb.IntegerProperty(default=0)
