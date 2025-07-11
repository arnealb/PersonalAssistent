import os.path
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from utils.ReaderInterface import get_service

# Alleen leestoegang
TOKEN_PATH = 'credentials/token_gmail.json'  
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
API_NAME = "gmail"
API_VERSION = "v1"


def read_latest_emails(n=5):
    service = get_service(TOKEN_PATH, SCOPES, API_NAME, API_VERSION)
    results = service.users().messages().list(userId='me', maxResults=n).execute()
    messages = results.get('messages', [])

    if not messages:
        print("Geen e-mails gevonden.")
        return

    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = txt.get('payload', {})
        headers = payload.get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(geen onderwerp)")
        sender = next((h['value'] for h in headers if h['name'] == 'From'), "(onbekend)")
        snippet = txt.get('snippet', '')

        print(f"Van: {sender}")
        print(f"Onderwerp: {subject}")
        print(f"Preview: {snippet}")
        print("-" * 40)

if __name__ == "__main__":
    read_latest_emails()
