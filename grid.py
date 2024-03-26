
import numpy as np
from enum import Enum


"""
Connect four grid class
"""

class markerType(Enum):
    EMPTY = 0
    PINK  = 1
    BLUE  = 2

#Number of connections for a win condition
winConnNum = 4
    
class grid:

    def __init__(self, rowCount, colCount) -> None:
        
        #Initialise empty grid
        self.matrix = np.zeros((rowCount, colCount))

        #Set Row and Column numbers
        self.colNum = colCount
        self.rowNum = rowCount

    #Drops a marker into the grid
    def addMarker(self, column, markerType):
        

        selectedColumn = self.matrix[:, column]

        #Check column isnt full
        if all(selectedColumn != 0):
            print("column full")
            return False

        #Place marker in lowest spot
        
        """
        Flip column
        Find lowest empty row
        Place token in matrix (via known column and found row)
        """
            



    #Prints the current grid status
    # 0 represents an empty slot - 1 represents player 1, 2 represents player 2 
    def printGrid(self):
        print(self.matrix)


    #Checks if there are four in a row
    def checkConnect(self):

        #Iterate through rows and columns, check all surrounding

        
        #If same ENUM val, check in direction until winConnNum
        pass



if __name__ == "main":

 

    testGrid = grid(7, 6)


    testGrid.printGrid()