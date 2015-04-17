import json
import urllib
import httplib2
import googleapiclient.discovery as api_discovery
from oauth2client import client as oauth2_client

METADATA_SERVER = ('http://metadata/computeMetadata/v1/instance/service-accounts')
SERVICE_ACCOUNT = 'default'

def tasks():
    http = httplib2.Http()
    credentials = get_service(http)
    if credentials is not None:
        taskq = api_discovery.build('taskqueue', 'v1beta2', http=credentials.authorize(http))
        return taskq
    else:
        print 'No tasks queue....'
    
def storage():
    http = httplib2.Http()
    credentials = get_service(http)
    if credentials is not None:
        storage = api_discovery.build('storage', 'v1', http=credentials.authorize(http))
        return storage
    else:
        print 'No storage....'
      
    
def get_service(http):
    token_uri = '%s/%s/token' % (METADATA_SERVER, SERVICE_ACCOUNT)
    resp, content = http.request(token_uri, method='GET',
                                 body=None,
                                 headers={'Metadata-Flavor': 'Google'})
    if resp.status == 200:
        d = json.loads(content)
        access_token = d['access_token']  # Save the access token
        credentials = oauth2_client.AccessTokenCredentials(d['access_token'], 'my-user-agent/1.0')
        return credentials
    else:
        return None