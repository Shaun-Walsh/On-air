import BlynkLib
from time import sleep
from sense_hat import SenseHat
from sensor_listener import SensorListener
from capture_image import capture_image
from upload_image import upload_image

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 's-umIxfRuDOQUmMyDuk1iyFBs3jGJvdh'
IMAGE_PATH = "./images/sensehat_image.jpg"

# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Global variable to track light state
light_on = False

# Function to capture and upload an image
def capture_and_upload_image():
    capture_image(IMAGE_PATH)  # Capture an image
    result = upload_image(IMAGE_PATH)  # Upload the image and get the URL
    blynk.set_property(2, "urls", result)  # Update the widget with the image URL

# Motion detected callback
def motion_detected(data):
    global light_on
    print("Motion detected")
    
    # Log event in Blynk
    blynk.log_event("movement_event", "Motion Detected")
    
    # Trigger camera function to capture and upload image
    capture_and_upload_image()

    # Turn on virtual pin V0 to indicate motion detected
    blynk.virtual_write(0, 1)
    sleep(2)
    blynk.virtual_write(0, 0)

# Virtual pin handler for light control (V1)
@blynk.on("V1")
def handle_v1_write(value):
    global light_on
    button_value = value[0]
    print(f'Light control button value: {button_value}')
    
    if button_value == "1":
        sense.clear(0, 255, 0)  # Turn on the green light
        light_on = True
    else:
        sense.clear()  # Turn off the light
        light_on = False

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for Movement Events...")
    
    # Set up the motion listener on port 5000
    listener = SensorListener(port=5000)
    listener.callback = motion_detected
    listener.start()

    try:
        while True:
            # Process Blynk events
            blynk.run()
            
            # Send temperature data to Virtual Pin V0
            temperature = round(sense.temperature, 2)
            blynk.virtual_write(0, temperature)
            
            # Sleep for 2 seconds to avoid excessive CPU usage and limit updates
            sleep(2)

    except KeyboardInterrupt:
        print("Blynk application stopped.")
