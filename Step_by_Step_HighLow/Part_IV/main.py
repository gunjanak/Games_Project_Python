import pygame
from pygame.locals import *
import sys
import pygwidgets

from Game import *


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
background = pygwidgets.Image(window,(0,0),'/home/janak/Documents/Pygame/My_Python_Games/Game_Projects/Games_Project_Python/Step_by_Step_HighLow/Images/background.png')
newGameButton = pygwidgets.TextButton(window,(20,530),'New Game',width=100,height=45)
higherButton = pygwidgets.TextButton(window,(540,520),'Higher',width=120,height=55)
lowerButton = pygwidgets.TextButton(window,(340,520),'Lower',width=120,height=55)
quitButton = pygwidgets.TextButton(window,(880,530),'Quit',width=100,height=45)


#initializevariables
oGame = Game(window)

#loop forever
while True:

    #check for event
    for event in pygame.event.get():
        if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()
        
        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()


        


    #clear the window before drawing it again
    background.draw()


    #Draw the window elements
    #tell the game to draw itself
    oGame.draw()

    #Drawing Buttons
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()


    #update the window
    pygame.display.update()

    #slow things down a bit
    clock.tick(FRAMES_PER_SECOND)



