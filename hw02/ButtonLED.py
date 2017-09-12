#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

# Set up LEDs
LED1 = "GREEN"
LED2 = "RED"
LED3 = "GP1_4"
LED4 = "GP1_3"
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

#Set up Buttons
Button1 = "GP0_6"
Button2 = "GP0_5"
Button3 = "GP0_4"
Button4 = "GP0_3"
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)

GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)
GPIO.output(LED4, 1)

# Map buttons to LEDs
map = {Button1: LED1, Button2: LED2, Button3: LED3, Button4: LED4}

def updateLED(channel):
  print("channel = " + channel)
  state = GPIO.input(channel)
  GPIO.output(map[channel], state)
  print(map[channel] + " Toggled")


GPIO.add_event_detect(Button1, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(Button2, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(Button3, GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(Button4, GPIO.BOTH, callback=updateLED)

try:
  while True:
    time.sleep(100)

except KeyboardInterrupt:
  print("Cleaning Up")
  GPIO.cleanup()

GPIO.cleanup()




