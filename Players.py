import re
from Game import Move, Piece
import random
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
    generateGrid()
    '''
    def __init__(self,Token,pieces,grid,player_number,mode,Training):
        Player.__init__(self,Token,pieces,grid,player_number)
        self.Mode = mode
        self.previousState = None
        self.previousMove = None
        self.CurrentData = {}
        self.readData(grid,mode)
        self.Training = Training
        
    def readData(self,grid,mode):
        try:
            ReadFile = open(str(len(grid))+"data"+mode+".txt","r+")
        except:
            return 
        NewData = {}
        currentState = 1
        currentIndex = 0
        currentTurn = None
        currentST = None
        #Patterns
        EndPattern = re.compile("^END$")
        EndPattern2 = re.compile("^\t\tENDMOVES\n$")
        EndPattern3 = re.compile("^\tENDSTATES\n$")
        Pattern1 = re.compile("^Ai for "+mode+str(len(grid))+"\n$")
        Pattern2 = re.compile("^Turn (\d+):\n$")
        Pattern3 = re.compile("^\tState:([X,Y, ]{"+str(len(grid)*len(grid))+"})\n$")
        Pattern4 = re.compile("^\t\tMove:(\d+),(\d+) (\d+),(\d+)\n$")
        
        FileList = ReadFile.readlines()
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
                if bool(Pattern2.match(currentString)):
                    NewData[int(Pattern2.match(currentString).group(1))] = []
                    currentTurn = int(Pattern2.match(currentString).group(1))
                    currentState = 3
                #Matches EndPattern: Add Data to File, Final End
                elif bool(EndPattern.match(currentString)):
                    self.CurrentData = NewData
                else:
                    Error = True
            elif currentState == 3:
                #State number
                
                #Matches Pattern3: Create New State
                if bool(Pattern3.match(currentString)):
                    grid = self.generateGrid(len(grid),Pattern3.match(currentString).group(1))
                    currentST = State(grid)
                    NewData[currentTurn].append(currentST)
                    currentState = 4
                #Matches EndPattern3: Revert back to State 2, End States
                elif bool(EndPattern3.match(currentString)):
                    currentState = 2
                else:
                    Error = True
            elif currentState == 4:
                #Move Number
                
                #Matches Pattern4: Add Move to Statelist
                if bool(Pattern4.match(currentString)):
                    matchedGroup = Pattern4.match(currentString)
                    fromSpotX,fromSpotY,toSpotX,toSpotY = matchedGroup.group(1),matchedGroup.group(2),matchedGroup.group(3),matchedGroup.group(4)
                    currentST.AddMove(Move((int(fromSpotX),int(fromSpotY)),(int(toSpotX),int(toSpotY))))
                    currentState = 4
                
                #Matches EndPattern2: Revert back to State 3, End Moves
                elif bool(EndPattern2.match(currentString)):
                    currentState = 3
                else:
                    Error = True
            else:
                Error = True
            currentIndex += 1
        ReadFile.close()
        if Error == True:
            print("-----Error Reading Ai's Data File.-----")
                
        
        
    def processData(self,winValue):
        if winValue == True and (self.Mode == "Addition" or self.Mode == "Mixed"):
            self.AddMove(self.previousState,self.previousMove)
        elif winValue == False and (self.Mode == "Subtraction" or self.Mode == "Mixed"):
            self.RemoveMove(self.previousState,self.previousMove)
            
        self.saveData(self.grid,self.Mode)
        
    def nextMove(self,turnNumber):
        if not self.Training:
            print("Turn Number "+str(turnNumber)+", "+ self.getToken() + "'s turn")
        
        CurrentState = None
        if turnNumber in self.CurrentData:
            CurrentState = self.getState(turnNumber)
        else:
            CurrentState = self.generateDefaultState(turnNumber)
        
        self.previousState = CurrentState
        if CurrentState.Movelist == []:
            #No matter what the Ai does, it will always lose.
            randomList = []
            for pieces in self.getPieces():
                randomList += self.getAvailableMoves(pieces)
            CurrentMove = random.choice(randomList)
            self.previousMove = None
        else:
            CurrentMove = CurrentState.getMove()
            self.previousMove = CurrentMove
        return CurrentMove, self
         
    def getState(self,turnNumber):
        currentState = State(self.grid)
        for States in self.CurrentData[turnNumber]:
            if States == currentState:
                return States
        
        return self.generateDefaultState(turnNumber)
    
    def generateGrid(self,gridlength,compressionString):
        currentGrid = []
        currentRow = []
        for index in range(len(compressionString)):
            currentCharacter = compressionString[index]
            currentRow.append(Piece(index // gridlength, index % gridlength, currentCharacter))
            if index % gridlength == gridlength -1:
                currentGrid.append(currentRow)
                currentRow = []
        return currentGrid
    
    def AddMove(self,State,Move):
        if Move != None:
            State.AddMove(Move)
    
    def RemoveMove(self,State,Move):
        if Move != None:
            State.RemoveMove(Move)
    
    def generateDefaultState(self,turnNumber):
        currentST = State(self.copyGrid(self.grid))
        for piece in self.getPieces():
            for move in self.getAvailableMoves(piece):
                currentST.AddMove(move)
        if turnNumber not in self.CurrentData:
            self.CurrentData[turnNumber] = [currentST]
        else:
            self.CurrentData[turnNumber].append(currentST)
        return currentST
        
    
    def saveData(self,grid,mode):
        WriteFile = open(str(len(grid))+"data"+mode+".txt","w+")
        WriteFile.write("Ai for "+mode+str(len(grid))+"\n")
        for turnNumber, States in self.CurrentData.items():
            WriteFile.write("Turn %d:\n" % turnNumber)
            for State in States:
                compressedString = self.getCompressedString(State.grid)
                WriteFile.write("\tState:"+compressedString+"\n")
                for Moves in State.Movelist:
                    WriteFile.write("\t\tMove:"+str(Moves)+"\n")
                WriteFile.write("\t\tENDMOVES\n")
            WriteFile.write("\tENDSTATES\n")
        WriteFile.write("END")
        WriteFile.close()
            
    def getCompressedString(self,grid):
        compressString = ''
        for row in grid:
            for column in row:
                compressString += column.getToken()
                
        return compressString
    
    def copyGrid(self,grid):
        newGrid = []
        for row in range(len(grid)):
            currentRow = []
            for column in range(len(grid)):
                currentRow.append(Piece(row,column,grid[row][column].getToken()))
            newGrid.append(currentRow)
        return newGrid
class State:
    '''Responsible for holding the configuration and Movelist for a given grid
    Variables:
    grid
    Movelist
    
    Functions:
    AddMove()
    RemoveMove()
    getMove()
    '''
    def __init__(self,grid):
        self.grid = grid
        self.Movelist = []
        
    def AddMove(self,Move):
        self.Movelist.append(Move)
        
    def RemoveMove(self,Move):
        self.Movelist.remove(Move)
        
    def getMove(self):
        return random.choice(self.Movelist)
    
    def __eq__(self,other):
        for row in range(len(self.grid)):
            for column in range(len(self.grid)):
                if self.grid[row][column].getToken() != other.grid[row][column].getToken():
                    return False
        return True
    
    def __str__(self):
        s = ''
        for row in range(len(self.grid)):
            for column in self.grid[row]:
                s = s +"|" + column.getToken()
                
            s += "\n"
        return s        