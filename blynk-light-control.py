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

# Function to capture and upload an image
def capture_and_upload_image():
    capture_image(IMAGE_PATH)  
    result = upload_image(IMAGE_PATH) 
    blynk.set_property(2, "urls", result) # Update the urls property of widget attached to Datastream2 (virtual pin V2)

# Motion detected callback
def motion_detected(data):
    print("Motion detected")
    blynk.log_event("movement_event", "Motion Detected")
# Call image capture and upload function
    capture_and_upload_image()
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
   
    else:
        sense.clear()  # Turn off the light

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for Movement Events...")
    listener = SensorListener(port=5000)
    listener.callback = motion_detected
    listener.start()

    try:
        while True:
            blynk.run() # Process Blynk events
            sleep(2) # Add a short delay to avoid high CPU usage

    except KeyboardInterrupt:
        print("Blynk application stopped.")
