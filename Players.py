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
    isValidIndex()
    
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
        if self.isValidIndex((currentSpot[0]+nextX,currentSpot[1]+nextY)) and self.grid[currentSpot[0] + nextX][currentSpot[1] + nextY].getToken() == validToken:
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
     
    def isValidIndex(self,results):
        resultX = int(results[0])
        resultY = int(results[1])
        return resultX >= 0 and resultX < len(self.grid) and resultY >= 0 and resultY < len(self.grid)   
    
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
            
            
    def nextMove(self,turnNumber):
        toSpot, fromSpot, validInput = None, None, False
        print("Turn Number "+str(turnNumber)+", "+ self.getToken() + "'s turn")
        while (not validInput):
      
            #Asking for FromInput            
            fromInput = input("From (#,#):")
            matches = re.findall("\d+",fromInput)
            if len(matches) == 2:
                    fromSpot = (int(matches[0]),int(matches[1]))
            
            #Asking for ToInput
            toInput = input("To (#,#):")
            matches = re.findall("\d+",toInput)
            if len(matches) == 2:
                toSpot = (int(matches[0]),int(matches[1]))
            
            #Checking if it's a valid token
            if fromSpot != None and toSpot != None and len(fromSpot) == 2 and len(toSpot) == 2 and self.isValidIndex(fromSpot) and self.grid[fromSpot[0]][fromSpot[1]].getToken() == self.getToken():
                if Move(fromSpot,toSpot) in self.getAvailableMoves(self.grid[fromSpot[0]][fromSpot[1]]):
                    return Move(fromSpot,toSpot), self
                else:
                    print("Not a valid Move!")
            else:
                print("Not a valid Position!")
        
        
                
                
            
        
        
class ComputerPlayer(Player):
    '''Responsible for handling ComputerInput for Player
    Subclass to Player
    3 Modes:
    Addition - Adds another instance of the winning Move to the set when winning a game
    Subtraction - Removes the instance of the losing Move from the set when losing a game
    Mixed - Does both
    
    Variables:
    Same as Player
    Mode
    previousState
    previousMove
    CurrentData
    
    Functions:
    AddMove()
    RemoveMove()
    saveData()
    readData()
    generateDefaultStates()
    getState()
    '''
    def __init__(self,Token,pieces,grid,player_number,mode):
        Player.__init__(self,Token,pieces,grid,player_number)
        self.Mode = mode
        self.previousState = None
        self.previousMove = None
        self.CurrentData = {}
        self.readData(grid,mode)
        
    def readData(self,grid,mode):
        ReadFile = open(str(len(grid))+"data"+mode+".txt","r+")
        NewData = {}
        currentState = 1
        currentIndex = 0
        #Patterns
        EndPattern = re.compile("^END\n$")
        EndPattern2 = re.compile("^\tEND\n$")
        EndPattern3 = re.compile("^\t\tEND\n$")
        Pattern1 = re.compile("^Ai for "+mode+str(len(grid))+"\n$")
        Pattern2 = re.compile("^Turn (\d+):\n$")
        Pattern3 = re.compile("^\tState:([X,Y, ]{%d})\n$" % len(grid) * len(grid))
        Pattern4 = re.compile("^\t\tMove:(\d+,\d+) (\d+,\d+)\n$")
        FileList = ReadFile.read()
        Error = False
        while currentIndex < len(FileList) and not Error:
            currentString = FileList[currentIndex]
            if currentState == 1:
                #Header
                if bool(Pattern1.match(currentString)):
                    currentState = 2
                else:
                    Error = True
            elif currentState == 2:
                #Turn Number
                
                #Matches Pattern2: Set Entry into NewData
                
                #Matches EndPattern: Add Data to File
            elif currentState == 3:
                #State number
                
                #Matches Pattern3: Create New State
                
                #Matches EndPattern2: Revert back to State 2
            elif currentState == 4:
                #Move Number
                
                #Matches Pattern4: Add Move to Statelist
                
                #Matches EndPattern3: Revert back to State 3
            else:
                Error = True
                
        
        
    def processData(self,winValue):
        if winValue == True and (self.Mode == "Addition" or self.Mode == "Mixed"):
            self.AddMove(previousState,previousMove)
        elif winValue == False and (self.Mode == "Subtraction" or self.Mode == "Mixed"):
            self.RemoveMove(previousState,previousMove)
            
        self.saveData(grid,mode)
        
    def nextMove(self,turnNumber):
        print("Turn Number "+str(turnNumber)+", "+ self.getToken() + "'s turn")
        
        CurrentState = None
        if turnNumber in self.CurrentData:
            CurrentState = self.getState()
        else:
            generateDefaultStates()
            CurrentState = self.getState()
        
        previousState = CurrentState
        CurrentMove = CurrentState.getMove()
        previousMove = CurrentMove
        return CurrentMove