#!/usr/bin/env python
import pygame, sys
from pygame.locals import *
import Adafruit_BBIO.GPIO as GPIO
import time

# Set up the frame
pygame.init()
size = [1000, 1000]
frame = pygame.display.set_mode(size)
frame.fill(WHITE)
pygame.display.set_caption("Use arrow key to move. Press 'd' to toggle delete mode.")

# Initialize the x, y position
currentX = 10
currentY = 10

# Set up buttons
Button_List = ["GP3_17", "GP3_20", "GP1_17", "GP1_25"]
for Button in Button_List:
  GPIO.setup(Left, GPIO.OUT)

while True: 
  time.sleep(100)
  pygame.draw.circle(frame, BLACK, [currentX, currentY], 1)
  pygame.display.update()
  if GPIO.input("GP3_17") and currentX > 0:
    currentX -= 1
  if GPIO.input("GP3_20") and currentY < 999:
    currentY += 1
  if GPIO.input("GP1_17") and currentY > 0:
    currentY -= 1
  if GPIO.input("GP1_25") and currentY < 999:
    currentY += 1

  for event in pygame.event.get(): 
    if event.type == bygame.QUIT: 
      sys.exit()
    elif event.type == KEYDOWN and event.key == K_d: 
      pygame.draw.circle(frame, WHITE, [currentX, currentY], 1)




