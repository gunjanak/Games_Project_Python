#card class
import pygame
import pygwidgets

class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('/home/janak/Documents/Pygame/My_Python_Games/Game_Projects/Games_Project_Python/Step_by_Step_HighLow/Images/BackOfCard.png')
    def __init__(self,window,rank,suit,value):
        self.window = window
        self.rank = rank
        self.suit= suit
        self.cardName = rank + ' of ' + suit
        self.value = value

        fileName = '/home/janak/Documents/Pygame/My_Python_Games/Game_Projects/Games_Project_Python/Step_by_Step_HighLow/Images/' + self.cardName + '.png'
        #set some starting location;
        # use setLoc below to change
        self.images = pygwidgets.ImageCollection(window,(0,0),{'front':fileName,'back':Card.BACK_OF_CARD_IMAGE},'back')

    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('front')

    def getName(self):
        return self.cardName
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def setLoc(self,loc):#cal the setLoc method of the ImageCollection
        self.images.setLoc(loc)

    def getLoc(self):#get the location form the ImageCollection
        loc = self.images.getLoc()
        return loc
    

    def draw(self):
        self.images.draw()