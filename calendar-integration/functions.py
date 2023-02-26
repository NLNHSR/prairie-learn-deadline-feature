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

        calendarList = service.calendarList().list().execute()["items"]
        for calendar in calendarList:
            if calendar["summary"] == "PrairieLearn Deadlines":
                plCalendarId = calendar["id"]

    return plCalendarId

def insertEvent(addEvent, plCalendarId):

    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)
    status = 2

    eventList = service.events().list(calendarId=plCalendarId).execute()["items"]
    eventToDeleteId = ""

    for event in eventList:
        if (event["summary"] == addEvent["summary"]):
            if (event["end"] == addEvent["end"]):
                status = 0
                break
            else:
                status = 1
                eventToDeleteId = event["id"]
                break
        else:
            status = 2

    if (status == 1):
            service.events().delete(calendarId=plCalendarId, eventId=eventToDeleteId).execute()
            service.events().insert(calendarId=plCalendarId, body=addEvent).execute()
    if (status == 2):
            service.events().insert(calendarId=plCalendarId, body=addEvent).execute()

    return print(status)




