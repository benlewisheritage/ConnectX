
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
        
        #check and set for winNum actually attainable in col and 
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
            -Only check after the appropriate number of counters
        1) Check horizontal (rows)
        2) Check Vertical   (columns)
        3) Check Diagonal   (???)
            
        
        """
    

        if(self.markerCount < ((self.markerWinNum * 2) - 1)):
            print("Not enough markers")
            return 0

        #Iterate through rows
        for rows in self.matrix:
            #Reset current marker type to check
            currMarkerType = 0
            markerCounter = 0
            for marker in rows:
                #Check marker is not null
                if(marker != 0):
                    #Update marker check
                    if(currMarkerType == 0):
                        currMarkerType = marker                
                    #Check marker is the same as current marker checking
                    if(marker == currMarkerType):
                        #increment checked marker count
                        markerCounter += 1
                        if(markerCounter == self.markerWinNum):
                            #this marker wins
                            print(f"ROW: 4 in a row in {rows}")
                            return currMarkerType
                    else:
                        #change marker check to current marker value and reset counter
                        currMarkerType = marker
                        markerCounter = 1
                else:
                    #reset counter and marker check
                    currMarkerType = 0
                    markerCounter = 0


        #Iterate through columns
        for col in self.matrix.T:
            #Determines how many are the same in a row (always 1 in a row)
            markerCounter = 1
            #Check theres enough slots filled
            if(np.count_nonzero(col) >= self.markerWinNum):
                currentMarkerType = 0
                #Count repeated markers (from the bottom)
                for marker in col[::-1]:
                                            
                    #If a 0, impossible to have markers above
                    if marker == 0:
                        break

                    #If marker is the same
                    if(marker == currentMarkerType):
                        markerCounter = markerCounter + 1
                        
                        if(markerCounter == self.markerWinNum):
                            print(f"COL: 4 in a row in: {col[::-1]}")
                            return currentMarkerType
                        
                    else:
                        #Set marker type
                        currentMarkerType = marker
                        markerCounter = 1
                        

            #print(f"No vertical four in a rows for {col}")
                        


        #Diagonal Check
                        
        #TODO rows and columns check if okay from top? (Do once at start then feed valid positions to diagonal checker)
        

        """
        Check that you start on a marker within a certain range
        i.e. 
        """

    #Recursive Diagonal Check
    def diagonalWinCheck(self, direction, rowPos, colPos, markerCount, currentMarkerType):

        #Determine the movement
        if direction == "UL":
            rowMove = -1
            colMove = -1
        elif direction == "UR":
            rowMove = -1
            colMove = 1
        else:
            print("INVALID DIRECTION")
            return -1
        
        #Update the position
        nextRow = rowPos + rowMove
        nextCol = colPos + colMove

        #Check the next position
        if self.matrix[nextRow, nextCol] == currentMarkerType:
            markerCount = markerCount + 1

            #If the fourth in the row
            if markerCount == self.markerWinNum:
                return currentMarkerType
            
            #Check the next marker
            else:
                return self.diagonalWinCheck(direction, nextRow, nextCol, markerCount, currentMarkerType)
            
        else:
            return 0

        


    #Empties the grid
    def gridWipe(self):
        self.matrix = np.zeros((self.rowNum, self.colNum))
        self.markerCount = 0

            
                                        



if __name__ == "__main__":

 
    
    player1Marker = markerType.BLUE
    player2Marker = markerType.PINK

    testGrid = grid(6, 7, markerWinNum = 4)


    testGrid.printGrid()

    #No win - not enough markers
    testGrid.checkConnect()
    

    #No Win - not enough markers
    testGrid.addMarker(2, player1Marker)
    testGrid.addMarker(1, player2Marker)    
    testGrid.addMarker(2, player1Marker)   
    testGrid.printGrid()
    testGrid.checkConnect()
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
    testGrid.printGrid()
    testGrid.checkConnect()
    testGrid.gridWipe()


    #Vertical Win Player 1 
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(2, player2Marker)    
    testGrid.addMarker(1, player1Marker) 
    testGrid.addMarker(2, player2Marker)  
    testGrid.addMarker(1, player1Marker)
    testGrid.addMarker(2, player2Marker)    
    testGrid.addMarker(1, player1Marker) 
    testGrid.printGrid()
    testGrid.checkConnect()    
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
    testGrid.printGrid()
    testGrid.checkConnect()    
    testGrid.gridWipe()




    #TODO: Diagonal Win Player 1 




    
