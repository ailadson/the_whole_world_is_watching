import os.path

# The email address for your GCS service account being used for signatures.
SERVICE_ACCOUNT_EMAIL = ('whole-world-is-watching@appspot.gserviceaccount.com')

GCS_API_ENDPOINT = 'https://storage.googleapis.com'

# Bucket name to use for writing example file.
BUCKET_NAME = 'whole-world-is-watching'

PRIVATE_KEY_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'secrets', 'www-d74ec83ddce8.der')
