# Proposal Document

# On Air

### Student Name: Shaun Walsh Student ID: 20005831

![https://media1.tenor.com/m/8GhHPlQ7pRcAAAAC/qa.gif](https://media1.tenor.com/m/8GhHPlQ7pRcAAAAC/qa.gif)

# **IoT "On Air" Sign Proposal**

## **Introduction**

This project aims to design and implement a smart "On Air" sign using a Raspberry Pi and Sense HAT. The sign will visually indicate availability (green for available, red for busy) and automate its behaviour based on Google Calendar events. Additional functionalities include integrating with Philips Hue smart lights to show availability to other areas of the property, and enhancing interactivity with a camera and infrared (PIR) sensor to monitor activity at the door during meetings. The goal is to create a multi-functional IoT device that is scalable and integrates seamlessly into smart home ecosystems. Use cases include for home workers, remote students, streamers, home recording musicians, amongst others. 

## Tools, Technologies and Equipment

## **Proposed Technologies**

### **Hardware**

1. **Raspberry Pi (with Sense HAT)**: Controls the LED matrix and gathers environmental data.
2. **PIR Sensor**: Detects motion near the sign for logging or alerts. (May potentially be a virtual implementation to prove concept)
3. **Camera Module**: Captures photos of visitors when the "On Air" sign is active.
4. **Smart Lights:** Adjustable throughout the property to indicate availability

### **Software**

1. **Google Calendar API**: Automatically adjusts the LED display based on meeting schedules.
2. **Philips Hue API**: Controls additional smart lights for enhanced notifications.
3. **Python**: Primary programming language for device logic and API integrations.
4. **Flask:** For a web-based control panel.
5. **Blynk:** To allow real time control in the initial implantation and for changes if a meeting etc is cancelled. 
6. **Packet Tracer:** Allows for use of a virtual motion sensor.
7. **VS Code**: Python development and control of the headless RPI through ssh.

### **Protocols**

- **MQTT/HTTP**: Communication between the Raspberry Pi and APi’s.
- **SSH**: Communicating with headless RPI from VS Code.

## **Deliverables**

1. **Basic Prototype**:
    - Manual control of Sense HAT LEDs via a mobile app.
2. **Intermediate Version**:
    - Integration with Google Calendar API for automated status updates.
3. **Advanced Features**:
    - Philips Hue smart light control.
    - IR sensor and camera functionality for capturing images of visitors.
4. **Enclosure**:
    - Custom 3D-printed or pre-made case for the Raspberry Pi and components.
    
    ![Logo](https://img.notionusercontent.com/s3/prod-files-secure%2F5938bc00-77d8-466a-8208-553814020976%2F08bd6d3b-e2ea-4d06-9cec-8af1df3fd4ec%2FWhatsApp_Image_2024-11-27_at_20.12.51_fb862ab6.jpg/size/w=2000?exp=1732830268&sig=Ph65l2mXobbBdcv6KDzTMYQy-vuAHE_PTMIs2in-uos)
    

## Project Repository

[https://github.com/Shaun-Walsh/On-air](https://github.com/Shaun-Walsh/On-air)
