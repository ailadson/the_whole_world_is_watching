import json
from google.appengine.api import taskqueue

def encode_video(incident):
    q = taskqueue.Queue('videoEncodeQueue')
    tasks = []
    data = {
        'cloud_id' : incident.cloud_id,
        'callback' : 'http://famous-crossing-850.appspot.com/encoded?id=%s&key=%s'%(incident.cloud_id, AUTH_CODE),
        'rawurl': '%s.raw'%(incident.cloud_id)
    }
    tasks.append(taskqueue.Task(payload=json.dumps(data), method='PULL'))
    q.add(tasks)
