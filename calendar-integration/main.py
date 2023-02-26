from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from functions import createEvent
from functions import createCalendar
from authenticator import authenticate
import os

if os.stat("token.json").st_size == 0:
    print('File is empty')
    authenticate()
else:
    print('File is not empty')

# Set up the Google Calendar API service object
creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
service = build('calendar', 'v3', credentials=creds)

# Define the event details
event = createEvent("TITLE", "DESCRIPTION", "LINK", (datetime.utcnow() + timedelta(hours=1)).isoformat())

print((datetime.utcnow() + timedelta(hours=2)).isoformat())

plCalendarId = createCalendar()

# Call the Calendar API to create the event
event = service.events().insert(calendarId=plCalendarId, body=event).execute()
print(f'Event created: {event.get("htmlLink")}')