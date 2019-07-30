import re
from Game import Move
class Player:
    '''Responsible for creating the Abstract Player
    Variables:
    Token
    pieces
    grid
    player_number
    Functions:
    getToken()
    getPieces()
    getAvailableMoves(Piece)
    nextMove()
    processData()
    
    '''
    def __init__(self,Token,pieces,grid,player_number):
        self.Token = Token
        self.pieces = pieces
        self.grid = grid
        self.player_number = player_number
    
    def getToken(self):
        return self.Token
    
    def getPieces(self):
        return self.pieces
    
    def getMove(self,moveList,currentSpot,nextX,nextY,validToken):
        if currentSpot[0] + nextX < len(self.grid) and currentSpot[1] + nextY < len(self.grid) and self.grid[currentSpot[0] + nextX][currentSpot[1] + nextY].getToken() == validToken:
            moveList.append(Move(currentSpot,(currentSpot[0]+nextX,currentSpot[1]+nextY)))
            
    def getAvailableMoves(self,Piece):
        #TODO:Finish function
        totalMovelist = []
        FromSpot = Piece.getPosition()
        if self.player_number == 1:
            #Checking Forward
            self.getMove(totalMovelist,FromSpot,1,0," ")

            #Checking right diagonally
            self.getMove(totalMovelist,FromSpot,1,1,"Y")
            
            #Checking left diagonally
            self.getMove(totalMovelist,FromSpot,1,-1,"Y")
        else:
            #Checking Forward
            self.getMove(totalMovelist,FromSpot,-1,0," ")
            
            #Checking right diagonally
            self.getMove(totalMovelist,FromSpot,-1,-1,"X")
            
            #Checking left diagonally
            self.getMove(totalMovelist,FromSpot,-1,1,"X")      
        
        return totalMovelist
    
    def nextMove(self):
        pass
    
    def processData(self):
        #Responsible for updating Data
        pass
    
    
    
class HumanPlayer(Player):
    '''Responsible for handling Human input for Player
    Subclass to Player
    '''
    def __init__(self,Token,pieces,grid,player_number):
        Player.__init__(self,Token,pieces,grid,player_number)
        
        
    def processData(self,winValue):
        if winValue:
            print("Congrats! " + self.Token + " wins!")
        else:
            print("Sorry! " + self.Token + " lost!")
            
            
    def isValidIndex(self,results,grid):
        resultX = int(results[0])
        resultY = int(results[1])
        return resultX >= 0 and resultX < len(grid) and resultY >= 0 and resultY < len(grid)
    
    def nextMove(self):
        pass
                
                
            
        
        
class ComputerPlayer(Player):
    '''Responsible for handling ComputerInput for Player
    Subclass to Player
    '''
    def __init__(self,Token,pieces,grid,player_number):
        Player.__init__(self,Token,pieces,grid,player_number)