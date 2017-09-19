#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

bus = smbus.SMBus(1)

# Set up button and alert
button = 'GP1_4'
alert = 'GP1_3'
GPIO.setup(alert, GPIO.IN)
GPIO.setup(button, GPIO.IN)

addressL = 0x49
addressR = 0x48

# Read and print out the temperature in F for both tmp101
def printTemp(x):
	tempL = bus.read_byte_data(addressL, 0)
	tempR = bus.read_byte_data(addressR, 0)
	print("Temperature from the Left: ", tempL*9/5+32, "F\n")
	print("Temperature from the Right: ", tempR*9/5+32, "F\n")

def printWarning(x):
	print("Temperature is out of range!")

# Set Thigh = 29C and Tlow = 23C, set TM = 1 in interrupt mode
bus.write_byte_data(addressR, 3, 0x1d)
bus.write_byte_data(addressR, 2, 0x1a)
bus.write_byte_data(addressR, 1, 0x80)

bus.write_byte_data(addressL, 3, 0x1d)
bus.write_byte_data(addressL, 2, 0x1a)
bus.write_byte_data(addressL, 1, 0x80)

GPIO.add_event_detect(button, GPIO.FALLING, callback=printTemp)
GPIO.add_event_detect(alert, GPIO.FALLING, callback=printWarning)

try:
  print("Running")
  while True:
    time.sleep(100)

except KeyboardInterrupt:
  print("Cleaning Up")
  GPIO.cleanup()

GPIO.cleanup()


