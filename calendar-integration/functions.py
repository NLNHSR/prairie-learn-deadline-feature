from __future__ import print_function
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def createEvent(assignment_title, assignment_description, assignment_link, deadline):
    event = {
        'summary': assignment_title,
        'location': assignment_link,
        'description': assignment_description,
        'start': {
            'dateTime': deadline,
            'timeZone': 'America/Chicago',
        },
        'end': {
            'dateTime': deadline,
            'timeZone': 'America/Chicago',
        },
    }

    return event

def insertEvent(event):

    # Set up the Google Calendar API service object
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    print("insertEvent function is running...")

    # Call the Calendar API to create the event
    service.events().insert(calendarId='plcalendar', body=event).execute()
    print('Event created: {event.get("htmlLink")}')

def createCalendar():

    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    print("createCalendar function is running...")
    calendarList = service.calendarList().list().execute()["items"]
    plCalendarId = "[]"
    plCalendarFound = False

    #This searches for the PrairieLearn Deadline calendar. If it found, it stores its ID
    for calendar in calendarList:
        if calendar["summary"] == "PrairieLearn Deadlines":
            plCalendarId = calendar["id"]
            plCalendarFound = True

    #If the PrairieLearn Deadlines calendar is not found, then it gets created and its ID gets fetched.
    if not plCalendarFound:
        calendar = {
            'summary': "PrairieLearn Deadlines",
            'description': 'This calendar contains upcoming deadline for PrairieLearn assignments. Please do not'
                           'rename this calendar!',
            'timeZone': 'America/Chicago'
        }
        service.calendars().insert(body=calendar).execute()
        for calendar in calendarList:
            if calendar["summary"] == "PrairieLearn Deadlines":
                plCalendarId = calendar["id"]

    return plCalendarId

