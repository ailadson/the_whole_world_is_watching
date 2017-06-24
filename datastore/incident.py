from incident_entity import IncidentEntity
from google.appengine.api import urlfetch
import json
import dateutil.parser
import tasks


class Incident(IncidentEntity):
    @classmethod
    def create(cls, cloud_id, uploader_ip):
        incident = cls(cloud_id=cloud_id, uploader_ip=uploader_ip)
        incident.put()
        return incident

    @classmethod
    def format_data(cls, params):
        data = {}
        bool_fields = (
            'disablility',
            'charged',
            'officerCharged',
            'convicted',
            'officerConvicted')
        float_fields = (
            'lat',
            'lng')
        int_fields = (
            'age')
        date_fields = (
            'date')

        for k, v in params.iteritems():
            if k == 'input_type':
                data[k] = v
            elif k.find('incident') == 0:
                field = k[9:-1]
                if field in float_fields:
                    data[field] = float(v)
                elif field in int_fields:
                    data[field] = int(v)
                elif field in bool_fields:
                    v = (True if v == 'yes' else False)
                    data[field] = v
                elif field in date_fields and v != '':
                    data[field] = dateutil.parser.parse(v).date()
                elif field == 'type':
                    bool_tags = params.getall('incident[type]')
                    for tag in bool_tags:
                        data[tag] = True
                else:
                    data[field] = v
        return data

    @classmethod
    def update_from_form(cls, cloud_id, data):
        incident = cls.query(cls.cloud_id==cloud_id).get()

        if incident is None: return

        incident.lat = data.get('lat')
        incident.lng = data.get('lng')
        incident.country = data.get('country')
        incident.state = data.get('state')
        incident.city_state = data.get('city_state', None)
        incident.city = data.get('city')
        incident.neighborhood = data.get('neighborhood')
        incident.zipCode = data.get('zipCode')


        incident.about = data.get('about')
        incident.brutal = data.get('brutal')
        incident.fatal = data.get('fatal')
        incident.docile = data.get('docile')

        incident.has_required_data = True

        if data.get('input_type') == 'optional':
            incident.user_email = data.get('user_email', None)

            incident.firstName = data.get('firstName', None)
            incident.lastName = data.get('lastName', None)
            incident.race = data.get('race', None)
            incident.gender = data.get('gender', None)
            incident.age = data.get('age', None)
            incident.disablility = data.get('disablility', None)
            incident.charged = data.get('charged', None)
            incident.chargedWith = data.get('chargedWith', None)
            incident.convicted = data.get('convicted', None)

            #officer data
            incident.officerFirstName = data.get('officerFirstName', None)
            incident.officerLastName = data.get('officerLastName', None)
            incident.officerBadge = data.get('officerBadge', None)
            incident.officerRace = data.get('officerRace', None)
            incident.officerGender = data.get('officerGender', None)
            incident.officerDept = data.get('officerDept', None)
            incident.officerCharged = data.get('officerCharged', None)
            incident.officerChargedWith = data.get('officerChargedWith', None)
            incident.officerConvicted = data.get('officerConvicted', None)

            incident.has_optional_data = True

        incident.add_location_data()
        incident.put()
        return incident

    def add_location_data(self):
        if self.lat is None or self.lng is None: return

        GEO_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"
        ARGS = "?latlng={0},{1}".format(self.lat, self.lng)

        locationData = {}
        jsonData = urlfetch.fetch(
            url=GEO_API_URL+ARGS,
            follow_redirects = False).content
        response = json.loads(jsonData)
        address_components = response['results'][0]['address_components']
        fields = {
            "neighborhood":"neighborhood",
            "administrative_area_level_1":"state",
            "administrative_area_level_2":"city_state",
            "locality":"city",
            "country":"country",
            "postal_code":"zipCode"
        }

        for i, component in enumerate(address_components):
            if i == 0: continue

            address_field = component['types'][0]
            if address_field in fields:
                field = fields[address_field];
                locationData[field] = component['long_name']

        self.populate(**locationData)

    def encode_video(self):
        if self.has_been_queued_for_encoding is False:
            tasks.encode_video(self)
            self.has_been_queued_for_encoding = True
            self.put()
