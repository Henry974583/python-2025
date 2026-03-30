import random
#class cin simulates a cin being tossed
#not that the name of the class has a capital letter for the firtst
#letter, this is a stnadard programming convention and should be followed

class Coin:
    #a class should begin with the _init_() method
    #this method executes first, as an intitializatoin of the class
    #the (self) parameter is a generally accepted naming convention
    #for the parameter within a class, and is requered
    
    #---data attributes---#
    #intitialize the data attribute with heads to indicate
    #the coin begins in a heads up position
    
    def __init__(self):
        self.__sideup = 'Heads'
        
    #---instance methods---#
    #the toss method generates a random number in the range of 0 though 1
    #if the number is 0, sideup is assigned heads
    #otherwise sideup is assigned tails
        
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            
    #get sideup method returns the current state of the coin
    #or the side that is facing up
            
    def get_sideup(self):
        return self.__sideup