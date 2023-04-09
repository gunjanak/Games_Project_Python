import random, pygame, sys
from pygame.locals import *

#frame per secont, the general speed of th program
FPS = 30

#window width in pixels 
WINDOWWIDTH = 640
#window height in pixels 
WINDOWHEIGHT = 480
#Speed boxes sliding reveals and covers
REVEALSPEED = 8
#Sizeof box height and width in pixels
BOXSIZE = 100
#gap between boxes
GAPSIZE = 20
#number of columns of icons
BOARDWIDTH = 4
#number of rows
BOARDHEIGHT = 4

#Board need to have an even number of boxes for pair mathes
assert(BOARDWIDTH*BOARDHEIGHT)%2 == 0, "Borad needs to have even number of boxes"

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE)))/2)


# Colors in pygame are represented by tuples of three integers [0-255]
#           R    G   B
GRAY     = (100,100,100)
NAVYBLUE = (60,60,100)
WHITE    = (255,255,255)
RED      = (255,0,0,)
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
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'



ALLCOLORS = (RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
ALLSHAPES = (DONUT,SQUARE,DIAMOND,LINES,OVAL)

assert len(ALLCOLORS)*len(ALLSHAPES)*2 >=BOARDWIDTH*BOARDHEIGHT


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0 #used to store x coordinate of mouse event
    mousey = 0 #used to store y coordinate of mouse event

    pygame.display.set_caption("Memory Game")

    mainBoard = getRandomizedBoard()
    #revealedBoxes = generateRevealedBoxesData(True)
    revealedBoxes = generateRevealedBoxesData(False)

    #firstSelection = None #Stores the (x,y) of the first box clicked

    DISPLAYSURF.fill(BGCOLOR)
    #startGameAnimation(mainBoard)
    drawBoard(mainBoard,revealedBoxes)


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)

 

    return revealedBoxes

def getRandomizedBoard():
    #get a list of every possible shape in every possible color
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))

    random.shuffle(icons)#randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH*BOARDHEIGHT/2) #calculate how many icons are needed
    icons = icons[:numIconsUsed]*2 #make two of each
    random.shuffle(icons)


    #create the board data structure, with randomly placed icons
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] #remove the icons as we assign them

        board.append(column)

    return board


def splitIntoGroupsOf(groupSize,theList):
    #split a list inot a list of lists, 
    #where inner lists have at mot groupSize number of items
    result = []
    for i in range(0,len(theList),groupSize):
        result.append(theList[i:i+groupSize])

    return result


def leftTopCoordsOfBox(boxx,boxy):
    #convert board cordinates into pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN

    return (left,top)


def getBoxAtPixel(x,y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)

            if boxRect.collidepoint(x,y):
                return (boxx,boxy)
            
    return (None,None)



def drawIcon(shape, color, boxx,boxy):

    quater = int(BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.5)

    left, top = leftTopCoordsOfBox(boxx,boxy)

    #draw the shapes
    if shape == DONUT:
        print("drwaing donut")
        pygame.draw.circle(DISPLAYSURF,color,(left+half,top+half),half-5)
        pygame.draw.circle(DISPLAYSURF,BGCOLOR,(left+half,top+half),quater-5)

    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF,color,(left+quater,top+quater,BOXSIZE-half,BOXSIZE-half))

    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF,color,((left+half,top),(left+BOXSIZE-1,top+half),(left+half,top+BOXSIZE-1),(left,top+half)))

    elif shape == LINES:
        for i in range(0,BOXSIZE,4):
            pygame.draw.line(DISPLAYSURF,color,(left,top+i),(left+i,top))
            pygame.draw.line(DISPLAYSURF,color,(left+i,top+BOXSIZE-1),(left+BOXSIZE-1,top+i))

    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF,color,(left,top+quater,BOXSIZE,half))


def getShapeAndColor(board,boxx,boxy):
    return board[boxx][boxy][0],board[boxx][boxy][1]



def drawBoxCovers(board,boxes,coverage):
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left,top,BOXSIZE,BOXSIZE))
        shape,color = getShapeAndColor(board,box[0],box[1])
        drawIcon(shape,color,box[0],box[1])

        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,coverage,BOXSIZE))


    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board,boxesToReveal):
    for coverage in range(BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToReveal,coverage)


def coverBoxesAnimation(board,boxesToCover):
    for coverage in range(BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToCover,coverage)


def drawBoard(board,revealed):
    print("Inside draw board")
    print(board)
 
    #Draw all the boxes in their covered or revealed state
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                #Draw a covered box
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
                print("Inside not revealed")
                

            else:
                print("Drawing")
                shape, color = getShapeAndColor(board,boxx,boxy)
                drawIcon(shape,color,boxx,boxy)
        #Redraw the screen and wait for a clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        pygame.time.wait(2000)




def drawHighlightBox(boxx,boxy):
    left,top = leftTopCoordsOfBox(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,HIGHLIGHTCOLOR,(left-5,top*5,BOXSIZE+10,BOXSIZE+10),4)


def startGameAnimation(board):
    #Randomly reveal 8 boxes at a time
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x,y))


    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8,boxes)
    drawBoard(board,coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board,boxGroup)
        coverBoxesAnimation(board,boxGroup)


if __name__ == '__main__':
    main()