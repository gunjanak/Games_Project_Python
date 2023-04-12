#card class
import pygame
import pygwidgets

class Card():
    BACK_OF_CARD_IMAGE = pygame.image.load('Images/BackOfCard.png')
    def __init__(self,window,rank,suit,value):
        self.window = window
        self.rank = rank
        self.suit= suit
        self.cardName = rank + ' of ' + suit
        self.value = value

        fileName = 'Images/' + self.cardName + '.png'
        #set some starting location;
        # use setLoc below to change
        self.imgaes = pygwidgets.ImageCollection(window,(0,0),{'font':fileName,'back':Card.BACK_OF_CARD_IMAGE},'back')

    def conceal(self):
        self.imgaes.replace('back')

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
        self.imgaes.setLoc(loc)

    def getLoc(self):#get the location form the ImageCollection
        loc = self.imgaes.getLoc()
        return loc
    

    def draw(self):
        self.imgaes.draw()

