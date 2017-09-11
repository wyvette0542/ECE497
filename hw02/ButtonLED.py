#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

# Set up LEDs
LED_List = ["LED_GREEN", "LED_RED", "GP3_1", "GP3_2"]
for LED in LED_List:
  GPIO.setup(LED, GPIO.OUT)

#Set up Buttons
Button_List = ["GP3_17", "GP3_20", "GP1_17", "GP1_25"]
for Button in Button_List:
  GPIO.setup(Left, GPIO.OUT)

# Map buttons to LEDs
ButtonLED_Map = {Button_List[0]: LED_List[0], Button_List[1]: LED_List[1], Button_List[2]: LED_List[2], Button_List[3]: LED_List[3]}

def updateLED(channel):
  print("channel = " + channel)
  state = GPIO.input(channel)
  GPIO.output(map[channel], state)
  print(map[channel] + " Toggled")

for Button in Button_List:
  GPIO.add_event_detect(Button, GPIO.BOTH, callback=updateLED)

try:
  while True:
    time.sleep(100)

except KeyboardInterrupt:
  print("Cleaning Up")
  GPIO.cleanup()

GPIO.cleanup()




