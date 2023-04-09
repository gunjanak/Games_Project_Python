import pygame,random
from memory_constants import *

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
    random.shuffle(icons)
    
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



#drawing Icons
def drawIcon(shape, color, boxx,boxy):

    quater = int(BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.5)

    left, top = leftTopCoordsOfBox(boxx,boxy)

    #draw the shapes
    if shape == DONUT:
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




#generate revealedBox data
def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)

    return revealedBoxes



#part 7
def drawBoard(board,revealed):
 
    #Draw all the boxes in their covered or revealed state
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                #Draw a covered box
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))

            else:
                #Drwa the (revealed icon)
                shape, color = getShapeAndColor(board,boxx,boxy)
                drawIcon(shape,color,boxx,boxy)



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


#Animating the revealbox 
def revealBoxesAnimation(board,boxesToReveal):
    #do the box reveal animation
    for coverage in range(BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToReveal,coverage)



def coverBoxesAnimation(board,boxesToCover):
    for coverage in range(BOXSIZE,(-REVEALSPEED)-1,-REVEALSPEED):
        drawBoxCovers(board,boxesToCover,coverage)

#Part 9
def hasWon(revealedBoxes):
    #Return True if all the boxes have been revealed
    for i in revealedBoxes:
        if False in i:
            return False

    return True 