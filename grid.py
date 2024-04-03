
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

    def __init__(self, rowCount, colCount, markerWinNum) -> None:
        
        if((markerWinNum > rowCount) or (markerWinNum > colCount)):
            markerWinNum = rowCount if(rowCount < colCount) else colCount
            

        #Initialise empty grid
        self.matrix = np.zeros((rowCount, colCount))

        #Set Row and Column numbers
        self.colNum = colCount
        self.rowNum = rowCount

        self.markerWinNum = markerWinNum

        #counter counter haha 
        self.markerCount = 0


    #Drops a marker into the grid
    def addMarker(self, column, markerType):
        
        #Make sure the column is valid
        if column > self.colNum - 1:
            print("Invalid Column")
            return        
        
        selectedColumn = self.matrix[:, column]

        #Check column isnt full
        if all(selectedColumn != 0):
            print("column full")
            return False

        #Go through the slots in the column
        rowSlot = self.rowNum - 1
        for slot in selectedColumn[::-1]:
            #Once empty slot found
            if slot == 0:
                break
            #Increase the slot 
            rowSlot = rowSlot -1 

        #Place the marker in the slot
        self.matrix[rowSlot, column] = markerType.value    

        #Increase the marker count
        self.markerCount = self.markerCount + 1  

            



    #Prints the current grid status
    # 0 represents an empty slot - 1 represents player 1, 2 represents player 2 
    def printGrid(self):
        print(self.matrix)


    #Checks if there are four in a row
    def checkConnect(self):

        """
        Notes:
            -Only check after the 7th counter
        1) Check horizontal (rows)
        2) Check Vertical   (columns)
        3) Check Diagonal   (???)
            
        
        """
    

        if(self.markerCount <= ((self.markerWinNum * 2) - 1)):
            print("Not enough markers")
            return 0

        #Iterate through rows
        for rows in self.matrix:
            #Reset current marker type to check
            markerCheck = 0
            markerCounter = 0
            for slot in rows:
                #Check slot is not null
                if(slot != 0):
                    #Update marker check 
                    if(markerCheck == 0):
                        markerCheck == slot                #Check slot is the same as current marker checking
                    if(slot == markerCheck):
                        #increment checked marker count
                        markerCounter += 1
                        if(markerCounter == self.markerWinNum):
                            #this marker wins
                            print(f"4 in a row in {rows}")
                            return markerCheck
                    else:
                        #change marker check to current slot value and reset counter
                        markerCheck = slot
                        markerCounter = 0
                else:
                    #reset counter and marker check
                    if(markerCheck != 0):
                        markerCheck = 0
                        markerCounter = 0


        #Iterate through columns
        for col in self.matrix:
            #Flag to determine 4 in a row
            markerCheck = 0
            #Determines how many are the same in a row (always 1 in a row)
            markerCounter = 1
            #Check theres enough slots filled
            if(np.count_nonzero(col) >= self.markerWinNum):
                currentMarker = 0
                #Count repeated markers
                for marker in col:
                                            
                    #If a 0, impossible to have markers above
                    if marker == 0:
                        break

                    #If marker is the same
                    if(marker == currentMarker):
                        markerCounter = markerCounter + 1
                        
                        if(markerCounter == self.markerWinNum):
                            print(f"4 in a row in: {col}")
                            return markerType
                        
                    else:
                        #Set marker type
                        currentMarker = marker
                        markerCounter = 1
                        
            
            if markerCheck == 0:
                print("No vertical four in a rows")

    #Empties the grid
    def gridWipe(self):
        self.matrix = np.zeros((self.rowNum, self.colNum))

            
                                        



if __name__ == "__main__":

 
    
    player1Marker = markerType.BLUE
    player2Marker = markerType.PINK

    testGrid = grid(7, 6, markerWinNum = 4)


    testGrid.printGrid()

    #No win - not enough markers
    testGrid.checkConnect()
    

    #No Win - not enough markers
    testGrid.addMarker(2, player1Marker)
    testGrid.addMarker(1, player2Marker)    
    testGrid.addMarker(2, player1Marker)   
    testGrid.checkConnect()
    testGrid.printGrid()
    testGrid.gridWipe()


    #No Win - no 4 in a row
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(1, player2Marker)    
    testGrid.addMarker(1, player1Marker) 
    testGrid.addMarker(1, player2Marker)  
    testGrid.addMarker(2, player1Marker)
    testGrid.addMarker(2, player2Marker)    
    testGrid.addMarker(2, player1Marker) 
    testGrid.addMarker(2, player2Marker)  
    testGrid.checkConnect()
    testGrid.printGrid()
    testGrid.gridWipe()


    #Vertical Win Player 1 
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(2, player2Marker)    
    testGrid.addMarker(1, player1Marker) 
    testGrid.addMarker(2, player2Marker)  
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(2, player2Marker)    
    testGrid.addMarker(1, player1Marker) 
    testGrid.checkConnect()
    testGrid.printGrid()
    testGrid.gridWipe()


    #Horizontal Win Player 2 
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(2, player2Marker)    
    testGrid.addMarker(2, player1Marker) 
    testGrid.addMarker(3, player2Marker)  
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(4, player2Marker)    
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(5, player2Marker)      
    testGrid.checkConnect()
    testGrid.printGrid()
    testGrid.gridWipe()



    

    


    #No win check
    testGrid.checkConnect()

