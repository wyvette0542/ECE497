#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

# Set up LEDs
LED_List = ["GREEN", "RED", "GP1_4", "GP1_3"]
for LED in LED_List:
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, 1)

#Set up Buttons
Button_List = ["GP0_6", "GP0_5", "GP0_4", "GP0_3"]
for Button in Button_List:
    GPIO.setup(Button, GPIO.IN)

# Map buttons to LEDs
map = {Button_List[0]: LED_List[0], Button_List[1]: LED_List[1], Button_List[2]: LED_List[2], Button_List[3]: LED_List[3]}

def updateLED(channel):
  print("channel = " + channel)
  state = GPIO.input(channel)
  GPIO.output(map[channel], state)
  print(map[channel] + " Toggled")

for Button in Button_List:
    GPIO.add_event_detect(Button, GPIO.BOTH, callback = updateLED)

try:
  while True:
    time.sleep(100)

except KeyboardInterrupt:
  print("Cleaning Up")
  GPIO.cleanup()

GPIO.cleanup()




