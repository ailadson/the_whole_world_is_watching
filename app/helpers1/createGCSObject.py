import cloudstorage as gcs

def createGCSObject(f, name):
    retry_params = gcs.RetryParams(initial_delay=0.2,
                                          max_delay=5.0,
                                          backoff_factor=2,
                                          max_retry_period=15)
    gcs.set_default_retry_params(my_default_retry_params)
    
    
    filename = '/net_wwwatching/'+name
    file = gcs.open(filename,mode='w',options={'x-goog-acl':'public-read'})
    file.write(f)
    file.close()