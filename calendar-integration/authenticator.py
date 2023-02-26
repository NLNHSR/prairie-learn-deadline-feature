from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def authenticate():
    # Set up the OAuth2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',  # Replace with the path to your client secret JSON file
        scopes=['https://www.googleapis.com/auth/calendar'],
    )

    # Run the authorization flow to obtain user consent and generate credentials
    creds = flow.run_local_server(port=0)

    # Save the credentials to a file (only needed for the first time)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

    # Create a Google Calendar API service object
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    calendar = service.calendars().get(calendarId='primary').execute()