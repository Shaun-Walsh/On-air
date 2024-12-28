import BlynkLib
from time import sleep
from sense_hat import SenseHat

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# Blynk authentication token
BLYNK_AUTH = 's-umIxfRuDOQUmMyDuk1iyFBs3jGJvdh'

# Initialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register handler for virtual pin V0 write event
@blynk.on("V0")
def handle_v0_write(value):
    button_value = value[0]
    print(f'Current button value: {button_value}')
    if button_value=="1":
        sense.clear()
    else:
        sense.clear()

# Main loop to keep the Blynk connection alive and process events
if __name__ == "__main__":
    print("Blynk application started. Listening for events...")
    try:
        while True:
            blynk.run()  # Process Blynk events
            sleep(2)  # Add a short delay to avoid high CPU usage
    except KeyboardInterrupt:
        print("Blynk application stopped.")