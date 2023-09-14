import pygame, sys
from pygame.locals import QUIT

color = (255, 0, 0)  #init color variable for background
pygame.init()  #init pygame
window = pygame.display.set_mode((500, 500))  #set window size
window.fill(color)  #set window color RGB val
pygame.display.set_caption("First Game")  #Sets title bar

x = 50  #x value for player location
y = 50  #y value for player location
width = 40  #player width
height = 60  #player height
vel = 15  #player speed

run = True   #setting a bool
while run:   #while run is True
  pygame.time.delay(100)

  for event in pygame.event.get():  #boilerplate for saying if we quite set bool to false
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()   #getting key presses for movement
  if keys[pygame.K_LEFT]:
    x -= vel                        #subtracting x vel for movement left, coordinate plane!
  if keys[pygame.K_RIGHT]:
    x += vel
  if keys[pygame.K_UP]:
    y -= vel
  if keys[pygame.K_DOWN]:
    y += vel
  window.fill((255, 0, 0))           #fill here with color of screen, disable to see why
  pygame.draw.rect(window, (0, 255, 0), (x, y, width, height))    #draw character rect

  pygame.display.update()           #update call 2nd to last
pygame.quit                         #quits, call last
