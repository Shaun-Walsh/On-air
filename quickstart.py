# This code is taken directly from here https://developers.google.com/calendar/api/quickstart/python#set-up-environment and modified to check for active events and turn on/off the Sense HAT lights accordingly.

import datetime
import os.path
import time
from sense_hat import SenseHat

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# ID of Calendar being used
calId = "1b07813367663daa2af43bd5f8e0e7e587545e02174dd01aff5462f8f58ad8e8@group.calendar.google.com"

# Initialize senseHAT
sense = SenseHat()

# This code was researched from here https://docs.python.org/3/library/time.html and here https://docs.python.org/3/library/datetime.html#module-datetime. It checks if there's an active event and turns the lights on/off."""
def check_active_event(events):
    now = datetime.datetime.utcnow()
    active = False

    for event in events:
        # Variables for the event's start and end times. 
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))

        start_dt = datetime.datetime.fromisoformat(start[:-1])  # Remove 'Z' if present
        end_dt = datetime.datetime.fromisoformat(end[:-1])      # Remove 'Z' if present

        # Check if current time is within the event's time range
        if start_dt <= now <= end_dt:
            active = True
            print(f"Active event: {event['summary']} ({start} - {end})")
            break

    # Turn Sense HAT lights on/off based on active status
    if active:
        sense.clear(0, 255, 0)  # Green light for active event
    else:
        sense.clear(0, 0, 0)  # Turn off lights if no active events

def main():
    """Fetch Google Calendar events and check for active ones."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        while True:  # Loop to keep checking for active events
            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
            print("Checking for active events...")
            events_result = (
                service.events()
                .list(
                    calendarId=calId,
                    timeMin=now,
                    maxResults=10,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])

            if not events:
                print("No upcoming events found.")
            else:
                check_active_event(events)

            time.sleep(60)  # Wait for 1 minute before checking again

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
