import threading
import get_service
import base64
import json
from perform_task import perform_task


print("Starting....")
PROJECT_ID = 's~famous-crossing-850'
QUEUE_NAME = 'videoEncodeQueue'

service = get_service.tasks()
result = service.tasks().lease(project=PROJECT_ID,taskqueue=QUEUE_NAME,leaseSecs=30,numTasks=1).execute()

if 'items' in result:
    for item in result['items']:
        t = threading.Thread(target=perform_task, args=(get_service.storage(), json.loads(base64.b64decode(item['payloadBase64']))))
        t.start()
        while t.is_alive():
            t.join(20)
            if t.is_alive():
                item.update(service.tasks().update(project=PROJECT_ID,taskqueue=QUEUE_NAME, newLeaseSeconds=30, body={'id':item['id'], 'kind': 'taskqueues#task', 'leaseTimestamp':item['leaseTimestamp'], 'queueName':QUEUE_NAME}, task=item['id']).execute())
        service.tasks().delete(project=PROJECT_ID, taskqueue=QUEUE_NAME, task=item['id']).execute()
else:
    print("No items in the task queue....")