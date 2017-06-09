from google.cloud import datastore



class Record():
    def __init__(self):
        self.client = datastore.Client()

        fields = {
            'lat' : 0.0,
            'lng' : 0.0,
            'country' : '',
            'state' : '',
            'city_state' : '',
            'city' : '',
            'neighborhood' : '',
            'zipCode' : '',

            'user_ip' : ''
            'date' : db.DateProperty()

            #arrested data
            'firstName' : '',
            'lastName' : '',
            'ethnicity' : '',
            'gender' : '',
            'age' : 0,
            'ability' : True,
            'charged' : True,
            'chargedWith' : '',
            'convicted' : True,

            #officer data
            'oFirstName' : '',
            'oLastName' : '',
            'badge' : '',
            'oRace' : '',
            'dept' : '',
            'oCharged' : True,
            'oChargedWith' : '',
            'oConvicted' : True,

            #incident data
            'about' : "",
            'assault' : True,
            'fatal' : True,
            'wrongful' : True,
            'interaction' : True,

            #meta data
            'promoted' : 0,
            'encoded' : True,
            'views' : 0
        }
