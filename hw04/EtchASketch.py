#!/usr/bin/env python3

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
import rcpy 
import rcpy.encoder as encoder
bus = smbus.SMBus(1)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

rcpy.set_state(rcpy.RUNNING)

# Set up the clean buttons
Clean = "GP1_4"
GPIO.setup(Clean, GPIO.IN)

delay = 0.5; # Delay between images

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Initialize the plot to be empty
game = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x800, 0x00, 0x00, 0x00, 0x00, 0x00]

currentX = 1
currentY = 1
current_e2 = 0
current_e3 = 0
while True:
	time.sleep(0.5)
	if rcpy.get_state() == rcpy.RUNNING:
		e2 = encoder.get(2) # read the encoders
		e3 = encoder.get(3)
	game[2 * currentX] = game[2 * currentX] | game[2 * currentX + 1]
	game[2 * currentX + 1] = 0x00
	temp = bus.read_byte_data(0x48, 0)
	if e2 - current_e2 > 0 and currentX < 7:
		currentX += int((e2 - current_e2) / (e2 - current_e2))
	if e2 - current_e2 < 0 and currentX > 0:
		currentX -= int((e2 - current_e2) / (e2 - current_e2))
	if e3 - current_e3 > 0 and currentY < 7:
		currentY += int((e3 - current_e3) / (e3 - current_e3))
	if e3 - current_e3 < 0 and currentY > 0:
		currentY -= int((e3 - current_e3) / (e3 - current_e3))
	if not GPIO.input(Clean) or temp > 28: # To clean up the frame, clean button pushed or temp exceed 28C/82.4F
		for i in range(0, 16): 
			game[i] = 0x00		
	game[2 * currentX + 1] = pow(2, currentY) # Cursor position
	bus.write_i2c_block_data(matrix, 0, game)
	current_e2 = e2
	current_e3 = e3




