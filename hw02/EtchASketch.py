#!/usr/bin/env python3
import pygame, sys
from pygame.locals import *
import Adafruit_BBIO.GPIO as GPIO

# Set up the frame
pygame.init()
size = [500, 500]
frame = pygame.display.set_mode(size)
frame.fill((255, 255, 255))
pygame.display.set_caption("Use arrow key to move. Press 'd' to toggle delete mode.")

# Initialize the x, y position
currentX = 20
currentY = 20

clock = pygame.time.Clock()

# Set up buttons
Left = "GP0_6"
Up = "GP0_5"
Down = "GP0_4"
Right = "GP0_3"
GPIO.setup(Left, GPIO.IN)
GPIO.setup(Up, GPIO.IN)
GPIO.setup(Down, GPIO.IN)
GPIO.setup(Right, GPIO.IN)

while True: 
  clock.tick(10)
  pygame.draw.circle(frame, (0, 0, 0), [currentX, currentY], 2)
  pygame.display.update()
  # Determine movement
  if GPIO.input(Left) and currentX > 1:
    currentX -= 2
  if GPIO.input(Down) and currentY < 498:
    currentY += 2
  if not GPIO.input(Up) and currentY > 1:
    currentY -= 2
  if not  GPIO.input(Right) and currentX < 498:
    currentX += 2

  # Click QUIT to quit the game and press 'd' from the keyboard to delete
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == KEYDOWN and event.key == K_d: 
      frame.fill((255, 255, 255))




