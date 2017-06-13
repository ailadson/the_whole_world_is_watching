import base64
import datetime
import md5
import sys
import time
import uuid
import json

import Crypto.Hash.SHA256 as SHA256
import Crypto.PublicKey.RSA as RSA
import Crypto.Signature.PKCS1_v1_5 as PKCS1_v1_5

from cloud_storage import conf

client_id_email = conf.SERVICE_ACCOUNT_EMAIL
gcs_api_endpoint = conf.GCS_API_ENDPOINT
bucket_name = conf.BUCKET_NAME

def get_signed_url_upload_endpoint():
    path = '/{0}/uploads/{1}.raw'.format(bucket_name, str(uuid.uuid4()))
    md5_digest = ''#base64.b64encode(md5.new(path).digest())
    base_url, query_params = _makeUrl(
        'PUT', path, 'application/octet-stream', md5_digest)

    headers = {}
    # headers['Content-MD5'] = md5_digest
    headers['content-Type'] = 'application/octet-stream'

    return json.dumps({
      'method': 'PUT', 'url' : base_url, 'params' : query_params, 'headers' : headers
    })

def _base64Sign(plaintext):
    keytext = open(conf.PRIVATE_KEY_PATH, 'rb').read()
    private_key = RSA.importKey(keytext)

    shahash = SHA256.new(plaintext)
    signer = PKCS1_v1_5.new(private_key)
    signature_bytes = signer.sign(shahash)
    return base64.b64encode(signature_bytes)

def _makeSignatureString(verb, path, content_md5, content_type, expiration):
    signature_string = ('{verb}\n'
                        '{content_md5}\n'
                        '{content_type}\n'
                        '{expiration}\n'
                        '{resource}')
    return signature_string.format(verb=verb,
                                   content_md5=content_md5,
                                   content_type=content_type,
                                   expiration=expiration,
                                   resource=path)

def _makeUrl(verb, path, content_type='', content_md5='', expiration=''):
    base_url = '%s%s' % (gcs_api_endpoint, path)

    expiration = (datetime.datetime.now() + datetime.timedelta(hours=1))
    expiration = int(time.mktime(expiration.timetuple()))

    signature_string = _makeSignatureString(
        verb, path, content_md5, content_type, expiration)
    signature_signed = _base64Sign(signature_string)

    query_params = {'GoogleAccessId': client_id_email,
                    'Expires': str(expiration),
                    'Signature': signature_signed}
    return base_url, query_params
