import pygame
from pygame.locals import *
import sys
import pygwidgets


#define constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

#initialize the world
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("The Card Game")

#load assets: imgaes,sounds
background = pygwidgets.Image(window,(0,0),'Images/background.png')



#loop forever
while True:

    #check for event
    for event in pygame.event.get():
        if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
            pygame.quit()
            sys.exit()


    #clear the window before drawing it again
    background.draw()

    #update the window
    pygame.display.update()

    #slow things down a bit
    clock.tick(FRAMES_PER_SECOND)



