import subprocess
import os
import urllib2
import get_service
import base64

def perform_task(service, payload):
    #get url for raw
    #payload = base64.b64decode(item['payloadBase64'])
    
    rawurl = payload['rawurl']
    vid_id = payload['id']
    callback = payload['callback']
    
    #get the file from gcs
    rawvid = service.objects().get_media(bucket='net_wwwatching',object=rawurl).execute()
    vidfile = open(rawurl,'wb')
    vidfile.write(rawvid)
    vidfile.close()
    
    #convert to mp4,ogg,webm...
    encode_video(rawurl,'%s.mp4'%vid_id)
    encode_video(rawurl,'%s.webm'%vid_id)
    encode_video(rawurl,'%s.ogv'%vid_id)
    
    #clean up..
    os.remove(rawurl)
    
    make_callback(callback)
    
def encode_video(rawfile,newfile):
    #create video
    subprocess.call(['ffmpeg', '-i', rawfile, newfile])
    #move to google cloud
    gcsname = "gs://net_wwwatching/%s" % newfile
    subprocess.call(['gsutil', 'cp', newfile, gcsname])
    subprocess.call(['gsutil','acl','set','public-read', gcsname])
    #clean up
    os.remove(newfile)
    
def make_callback(cb):
        result = urllib2.urlopen(url)
        if result.code == 200:
            pass
        else:
            print('Callback to appengine failed....Check record %s in datastore'%vid_id)
            

    