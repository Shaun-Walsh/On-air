import datetime
import os.path
import time
from sense_hat import SenseHat
from dateutil.parser import isoparse

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# ID of Calendar being used
calId = "1b07813367663daa2af43bd5f8e0e7e587545e02174dd01aff5462f8f58ad8e8@group.calendar.google.com"

# Initialize sesnehat object
sense = SenseHat()

# Colour Variables
GREEN = (0, 255, 0)  # RGB for green
OFF = (0, 0, 0)    # RGB for red

# # Time fucntions in this code were researched from here https://docs.python.org/3/library/time.html and here https://docs.python.org/3/library/datetime.html#module-datetime. 
# It checks if there's an active event by examining if the current time is within the event's start and end times, if it is, it turns on the green light on the Sense HAT, otherwise it turns off the lights.

# Global variable to track event and state
current_event_id = None
new_event = True

# Function to check active events
def check_active_event(events):
    global current_event_id, new_event
    now = datetime.datetime.now(datetime.timezone.utc)
    active_event = None

    # Check if any event is currently active
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))

        # Parse start and end times as timezone-aware datetime objects
        start_dt = isoparse(start)
        end_dt = isoparse(end)

        # Check if current time is within the event's time range
        if start_dt <= now <= end_dt:
            active_event = event
            break

    if active_event:
        event_id = active_event["id"]
        if event_id != current_event_id:
            # New event detected, reset new_event flag
            current_event_id = event_id
            new_event = True

        if new_event:
            # Turn on light only once for the event
            sense.clear(GREEN)
            print(f"Light turned on for event: {active_event['summary']}")
            new_event = False  # Prevent turning on the light again
    else:
        # No active event, reset everything
        if current_event_id is not None:
            print(f"Event {current_event_id} has ended. Turning off lights.")
        sense.clear(OFF)
        current_event_id = None
        new_event = True

# This code is taken directly from here https://developers.google.com/calendar/api/quickstart/python#set-up-environment and modified to fit the project.
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

# Place into a loop to keep checking for active events every 30 seconds
        while True:  
            # Call the Calendar API
            now = datetime.datetime.now(datetime.timezone.utc).isoformat()  # UTC timestamp with timezone
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

            time.sleep(30)  # Wait for 30 seconds before checking again

         # Short delay to prevent high CPU usage
        time.sleep(0.1)

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
