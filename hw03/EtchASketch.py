#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Set up buttons
Left = "GP0_6"
Up = "GP0_5"
Down = "GP0_4"
Right = "GP0_3"
Clean = "GP1_4"
GPIO.setup(Left, GPIO.IN)
GPIO.setup(Up, GPIO.IN)
GPIO.setup(Down, GPIO.IN)
GPIO.setup(Right, GPIO.IN)
GPIO.setup(Clean, GPIO.IN)

delay = 0.5; # Delay between images

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Initialize the plot to be empty
game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x800, 0x00, 0x00, 0x00, 0x00, 0x00]

currentX = 0
currentY = 0
while True:
	time.sleep(0.1)
	game[2 * currentX] = game[2 * currentX] | game[2 * currentX + 1]
	game[2 * currentX + 1] = 0x00
	temp = bus.read_byte_data(0x48, 0)
	if not GPIO.input(Right) and currentX > 0:
		currentX -= 1
	if GPIO.input(Down) and currentY < 7:
		currentY += 1
	if not GPIO.input(Up) and currentY > 0:
		currentY -= 1
	if GPIO.input(Left) and currentX < 7:
		currentX += 1
	if not GPIO.input(Clean) or temp > 28: # To clean up the frame, clean button pushed or temp exceed 28C/82.4F
		for i in range(0, 16): 
			game[i] = 0x00		
	game[2 * currentX + 1] = pow(2, currentY) # Cursor position
	bus.write_i2c_block_data(matrix, 0, game)




