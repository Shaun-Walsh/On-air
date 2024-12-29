# On-air
This project aims to design and implement a smart "On Air" sign using a Raspberry Pi and Sense HAT. The sign will visually indicate availability (clear for available, green for busy) and automate its behaviour based on Google Calendar events.

The application includes motion detection, image capture, and the ability to control the Sense HAT’s LED matrix through Blynk. This update allows for automated camera captures when motion is detected, all while maintaining the ability to manually control the lights via Blynk.

![https://media1.tenor.com/m/8GhHPlQ7pRcAAAAC/qa.gif](https://media1.tenor.com/m/8GhHPlQ7pRcAAAAC/qa.gif)

🔧 **Key Features:**
- **Google Calendar Integration**:
  - Automatically checks a specific Google Calendar for upcoming and ongoing events.
  - Supports both **dateTime** and **all-day events**.
  
- **Real-Time Event Detection**:
  - Continuously checks for active events every 60 seconds.
  - If an event is active:
    - Turns the Sense HAT light **green** to indicate an active event.
  - If no events are active:
    - Turns the lights **off**.

- **Authentication and Security**:
  - Uses OAuth 2.0 for secure access to your Google Calendar.
  - Stores user credentials locally in `token.json` for subsequent use.
  
- **Motion Detection**:
  - Real-time motion sensing: Automatically triggers the camera when motion is detected.
  - Image Capture and Upload: Captures an image when motion is detected and uploads it to a remote server.
  
- **Blynk Integration**:
  - Manual Light Control: Use Blynk's virtual pin (V1) to control the Sense HAT light (green for on, off when switched off).

- **Image Upload**:
  - Remote Image Upload: Uploads captured images to a server, with URL updates to Blynk’s data stream (V2).

🛠️ **How It Works:**

1. The script authenticates with Google Calendar using credentials stored in `credentials.json`.

2. It queries the Google Calendar API for events using the provided `calId`.

3. Based on the event's start and end times:
   - If the current time is within an event's range, the LED matrix on the Sense HAT lights up green.
   - If no events are active, the LED matrix turns off.

4. **Motion Detection**:
   - The system listens for motion via UDP packets.
   - Upon detecting motion, it triggers an image capture function and uploads the image to a server.
   
5. **Blynk Light Control**:
   - The user can control the Sense HAT LED matrix through the Blynk app, turning it on (green) or off (off).
   
7. **Image Capture and Upload**:
   - When motion is detected, an image is captured using the Raspberry Pi camera and uploaded to a remote server on glitch.
   - The URL for the uploaded image is then sent to Blynk to update a widget (V2).

📋 **Prerequisites:**

### Hardware:
- Raspberry Pi with Sense HAT installed.
- Raspberry Pi camera module (for image capture).
  
### Software:
- Blynk app setup (with virtual pins V1, V2 configured).
  
### Python Libraries:
- `blynklib`
- `sense_hat`
- `picamera2`
- `google-auth`
- `dateutil.parser`
- `google.auth.transport.requests`
- `google_auth_oauthlib.flow`
- `googleapiclient.discovery`
- `google.oauth2.credentials`
- `googleapiclient.errors`


### Google calendar setup:
  - A shared or personal Google Calendar to monitor events.
  - A `credentials.json` file generated from the Google Cloud Console.

### External Services:
- **Image Upload Service**: Ensure a working upload endpoint for images (e.g., Glitch API or custom server).

📖 **Usage Instructions:**

1. **Set up the environment**:
   - Install required Python libraries:
     ```bash
     pip install blynklib sense-hat picamera2...
     ```

2. **Set up Google API Credentials**:
   - Follow the instructions at [Google Calendar API Quickstart](https://developers.google.com/calendar/api/quickstart/python) to create a `credentials.json` file.
   - Save the file in the same directory as the script.
   - Continue the OAUTH flow per instructions

3. **Set up the Blynk app**:
   - Create a project in Blynk and configure virtual pins V1 (light control), and V2 (image URL).

4. **Run the Scripts**:
   - Run the following scripts:
     - `python quickstart.py` - Checks calendar for events and controls lights.
     - `python blynk-light-control.py` - Manages light control and temperature monitoring via Blynk.

**Known Issues**:
- If an event is passed to the app without a title the app will crash.

**MIT License**:

Copyright (c) [2024] [Shaun Walsh]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

