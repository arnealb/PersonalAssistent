
import os.path
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build





def get_service(TOKEN_PATH, SCOPES, api_name, api_version):
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/gmail_credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=0, prompt='consent')
            with open(TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())

    return build(api_name, api_version, credentials=creds)
