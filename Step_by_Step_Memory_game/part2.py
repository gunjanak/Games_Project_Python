import pygame, random,sys
from pygame.locals import *


#frames per second, the general speed of the program
FPS = 30
#window width in pixels
WINDOWWIDTH = 640
#Window height in pixels
WINDOWHEIGHT = 480
#Boxsize
BOXSIZE = 90
#GAPsize
GAPSIZE = 20
#Number of columns of icons 
BOARDWIDTH = 4
#Number of rows of icons
BOARDHEIGHT = 4

#Board need to have an even numberof boxes for pairs of matches
assert(BOARDWIDTH*BOARDHEIGHT)%2 == 0, "Board needs to have even number of Boxes"

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH*(BOXSIZE+GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE+GAPSIZE)))/2)


#            R   G   B
GRAY     = (100,100,100)
NAVYBLUE = (60,60,100)
WHITE    = (255,255,255)
RED      = (255,0,0)
GREEN    = (0,255,0)
BLUE     = (0,0,255)
YELLOW   = (255,255,0)
ORANGE   = (255,128,0)
PURPLE   = (255,0,255)
CYAN     = (0,255,255)


BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE



DONUT = 'donut'
SQUARE= ' square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
ALLSHAPES = (DONUT,SQUARE,DIAMOND,LINES,OVAL)

assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDHEIGHT*BOARDWIDTH, "Board is too big for the number of shapes/colors defined"


def main():
    global FPSCLOCK,DISPLAYSURF
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock() #this will allow us to track time since last time the screen has been refreshed
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))


    pygame.display.set_caption("Memory Game")




    while True:

        #Drawing the window
        DISPLAYSURF.fill(BGCOLOR)

        drawBoard() #part 2

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()


        #Redraw the screen and wait a clock tick
        pygame.display.flip()
        FPSCLOCK.tick(FPS)



def leftTopCoordsOfBox(boxx,boxy): #part 2
    #convert the board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE)+YMARGIN

    return (left,top)

def drawBoard(): #part 2
    #Draw all the boxes
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
           

            pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))


if __name__ == "__main__":
    main()
