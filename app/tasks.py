import json
from google.appengine.api import taskqueue

AUTH_CODE = '31fcfe679c604c68944c8041af253b02'

def create(record):
    q = taskqueue.Queue('videoEncodeQueue')
    tasks = []
    data = {
        'id' : record.id,
        'callback' : 'http://famous-crossing-850.appspot.com/encoded?id=%s&key=%s'%(record.id, AUTH_CODE),
        'rawurl': '%s.raw'%(record.id)
    }
    tasks.append(taskqueue.Task(payload=json.dumps(data), method='PULL'))
    q.add(tasks)


