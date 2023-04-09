import pygame
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

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
FPSCLOCK = pygame.time.Clock()

#speed of boxes sliding reveals and covers
REVEALSPEED = 8

assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDHEIGHT*BOARDWIDTH, "Board is too big for the number of shapes/colors defined"

