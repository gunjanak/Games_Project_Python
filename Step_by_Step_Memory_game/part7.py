import pygame, random,sys
from pygame.locals import *

from memory_functions import *
from memory_constants import *

def main():
    
    pygame.init()
    
     #this will allow us to track time since last time the screen has been refreshed
    
    pygame.display.set_caption("Memory Game")
  
    mousex = 0 #used to store x coordinate of mouse event
    mousey = 0 #used to store y coordinate of mouse event

    #The function to generate a random board
    mainBoard = getRandomizedBoard()
    
    #part 7
    revealedBoxes = generateRevealedBoxesData(False) 

    while True:

        #Drawing the window
        DISPLAYSURF.fill(BGCOLOR)
        

        #drawRevealedBoard(mainBoard)
        drawBoard(mainBoard,revealedBoxes)
         

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            
            elif event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                mouseClicked = True

        boxx,boxy = getBoxAtPixel(mousex,mousey)
        if boxx != None and boxy != None:

            #part 7
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx,boxy)

            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard,[(boxx,boxy)])


        
        #Redraw the screen and wait a clock tick
        pygame.display.flip()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()
