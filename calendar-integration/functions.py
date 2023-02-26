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
    status = 1
    titlesList = []

    eventsInCalendar = service.events().list(calendarId=plCalendarId).execute()["items"]
    for event in eventsInCalendar:
        titlesList.append(event["summary"])

    print(titlesList)

    if addEvent["summary"] not in titlesList:
        service.events().insert(calendarId=plCalendarId, body=addEvent).execute()

    return print(status)

def readDictionaryIntoList(dict):

    gcEventList = []

    for k in dict:
        for assignment in dict[k]:
            if assignment['most_relevant_date'] is not None:
                title = assignment['course_name'] + ' - ' + assignment['assignment_name'] + "  (" + assignment['most_relevant_percentage'] + ")"
                link = assignment['link']
                time = assignment['most_relevant_date'].isoformat()
                gcEventList.append(createEvent(title, '.', link, time))
    return gcEventList