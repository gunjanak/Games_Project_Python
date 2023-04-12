import pygame, random,sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window


from memory_functions import *
from memory_constants import *

def main():
    
    pygame.init()
    pygame.display.set_caption("Memory Game")
  
    mousex = 0 #used to store x coordinate of mouse event
    mousey = 0 #used to store y coordinate of mouse event

    #The function to generate a random board
    mainBoard = getRandomizedBoard()
    
    #part 7
    revealedBoxes = generateRevealedBoxesData(False) 

    #part 8
    #store the (x,y) of the first box clicked
    firstSelection = None


    while True:

        #part 8
        mouseClicked = False
        #Drawing the window
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard,revealedBoxes)
         

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
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

                #part 8
                #set the box as revealed
                revealedBoxes[boxx][boxy]=True

                if firstSelection == None:#the current box was the first box clicked
                    firstSelection = (boxx,boxy)

                else:#the current box was the second box clicked
                    #check if there is a match between the two icons
                    icon1Shape, icon1Color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                    icon2Shape, icon2Color = getShapeAndColor(mainBoard,boxx,boxy)
                    

                    if icon1Shape != icon2Shape or icon1Color != icon2Color:
                        #icons do not match recover up both selections
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])

                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False

                    #part 9
                        
                    elif hasWon(revealedBoxes):
                        print("You did it")
                        
                        messagebox.showinfo('Winner','You did it')
                        
                    firstSelection = None

                     


        
        #Redraw the screen and wait a clock tick
        pygame.display.flip()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()
