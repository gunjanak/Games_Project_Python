#Generating a random board
#Part 3 highlighting the box with a cursor over it

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

    #Part 3
    mousex = 0 #used to store x coordinate of mouse event
    mousey = 0 #used to store y coordinate of mouse event

    #Part 4 
    #The function to generate a random board
    mainBoard = getRandomizedBoard()
    print("\n\n\n")
    print(mainBoard)




    while True:

        #Drawing the window
        DISPLAYSURF.fill(BGCOLOR)

        drawBoard() #part 2

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            #part 3
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
                mouseClicked = True

        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if boxx != None and boxy != None:
            drawHighlightBox(boxx,boxy)

            


        #Redraw the screen and wait a clock tick
        pygame.display.flip()
        FPSCLOCK.tick(FPS)


#part 4
def getRandomizedBoard():
    #Get a list of every possible shape in every possible color
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))

    random.shuffle(icons) #randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH*BOARDHEIGHT/2) #Calculate how many icons are needed
    icons = icons[:numIconsUsed]*2 #make two of each
    
    #Create the board data structure, with randomly placed icons
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] #remove the icons as we assign them

        board.append(column)

    return board



def leftTopCoordsOfBox(boxx,boxy): #part 2
    #convert the board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE)+YMARGIN

    return (left,top)

#Part 3
def getBoxAtPixel(x,y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)

            if boxRect.collidepoint(x,y):
                return(boxx,boxy)
            
    return (None,None)

def drawHighlightBox(boxx,boxy):
    left,top = leftTopCoordsOfBox(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,HIGHLIGHTCOLOR,(left-5,top-5,BOXSIZE+10,BOXSIZE+10),4)

def drawBoard(): #part 2
    #Draw all the boxes
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
           

            pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))


if __name__ == "__main__":
    main()
