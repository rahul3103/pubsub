client_id = '179120194532-apl028ogkiej4a1ebhl9cdv0fe8a2k5g.apps.googleusercontent.com'
client_secret = '7u--bL8JxwYpJZRc5KpUXrD5'
redirect_uri = 'http://localhost:5000/callback'
authorization_base_url = 'https://accounts.google.com/o/oauth2/auth'
token_url = 'https://accounts.google.com/o/oauth2/token'
scope = ['https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.metadata']
user_id = 'me'

import os
import google.oauth2.credentials
from requests_oauthlib import OAuth2Session
from googleapiclient.discovery import build

google_auth = OAuth2Session(
    client_id,
    scope=scope,
    redirect_uri=redirect_uri)

authorization_url, state = google_auth.authorization_url(
    authorization_base_url,
    access_type='offline',
    prompt='consent',
    include_granted_scopes='true')

print(authorization_url) # run on chrome

url = 'return url'

token = google_auth.fetch_token(
    token_url,
    client_secret=client_secret,
    authorization_response=url)

access_token = token['access_token']

refresh_token = token['refresh_token']

credentials = google.oauth2.credentials.Credentials(
    access_token,
    refresh_token=refresh_token,
    token_uri=token_url,
    client_id=client_id,
    client_secret=client_secret)

service = build('gmail', 'v1', credentials=credentials)

request = {
    'labelIds': ['INBOX'],
    "labelFilterAction":'include',
    'topicName': 'projects/test-work-206411/topics/newtopic'
    }

history_ids = service.users().watch(userId=user_id, body=request).execute()

history = service.users().history().list(userId=user_id, startHistoryId=history_ids['historyId']).execute()
# This will give the all changes happened after the history Id

message = service.users().messages().get(userId=user_id, id=msg_id, format='minimal/full/raw/metadata').execute()
