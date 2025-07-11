import os.path
import datetime
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from utils.ReaderInterface import get_service

TOKEN_PATH = 'credentials/token_google_calendar.json'  # of token_calendar.json
SCOPES = ['https://www.googleapis.com/auth/calendar']
API_NAME = "calendar"
API_VERSION = "v3"



def get_upcoming_events(n=5):
    service = get_service(TOKEN_PATH, SCOPES, API_NAME, API_VERSION)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' = UTC
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=n, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print("Geen aankomende afspraken gevonden.")
        return

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start} - {event['summary']}")
