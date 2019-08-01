class Game:
    """Responsible for holding the state of the Game.
    Variables:
    grid
    turn
    player_one
    player_two
    winner
    Functions:
    isWin()
    nextMove()
    printState()
    ApplyMove()
    getWinner()
    """

    def __init__(self,player1: "Player" ,player2: "Player", grid = []):
        self.grid = grid
        self.turn = 0
        self.player_one = player1
        self.player_two = player2
    
    def isWin(self):
        isWinner = False
        player1Winner = True
        #Checking if Player1 pieces are all dead
        if len(self.player_one.getPieces()) == 0:
            player1Winner = False
            isWinner = True
        
        #Checking if player2 pieces are all dead
        if len(self.player_two.getPieces()) == 0:
            player1Winner = True
            isWinner = True
            
        #Check for Winner: Player1
        for piece in self.grid[len(self.grid)-1]:
            if piece.getToken() == self.player_one.getToken():
                player1Winner = True
                isWinner = True
                
        #Check for Winner: Player2
        for piece in self.grid[0]:
            if piece.getToken() == self.player_two.getToken():
                player1Winner = False
                isWinner = True        
        
        #Check for Stalemate
        for piece in self.player_one.getPieces():
            if all([1 if self.player_one.getAvailableMoves(piece) == [] else 0 for piece in self.player_one.getPieces()]):
                isWinner = True
                player1Winner = self.turn % 2 != 0
                
        if isWinner:
            self.winner = self.player_one if player1Winner else self.player_two
            self.player_one.processData(player1Winner)
            self.player_two.processData(not player1Winner)
            return True
        return False
    
    def nextMove(self):
        self.turn += 1
        if self.turn % 2 != 0:
            return self.player_one.nextMove(self.turn)
        return self.player_two.nextMove(self.turn)
    
    def ApplyMove(self,Move,player):
        fromX,fromY = Move.fromSpot
        toX,toY = Move.toSpot
        if self.grid[toX][toY].getToken() != " " and self.grid[toX][toY].getToken() != player.getToken():
            if player.getToken() == "X":
                self.player_two.getPieces().remove(self.grid[toX][toY])
            else:
                self.player_one.getPieces().remove(self.grid[toX][toY])
        self.grid[toX][toY] = self.grid[fromX][fromY]
        self.grid[fromX][fromY] = Piece(fromX,fromY," ")
        self.grid[toX][toY].updatePosition(toX,toY)
        print(player.getToken() +" moved to: " + "("+str(toX)+","+str(toY)+")")
    
    def printState(self):
        s = ' '
        for row in range(len(self.grid)):
            s = s + " " + str(row)
        print(s)
        for row in range(len(self.grid)):
            s = str(row)
            for column in self.grid[row]:
                s = s +"|" + column.getToken()
            print(s)
                
    def getWinner(self):
        return self.winner
            
class Piece:
    '''Responsible for holding the data about a single Piece in the game.
    Variables:
    x
    y
    Token
    Functions:
    getPosition()
    getToken()
    '''
    def __init__(self,x,y,Token):
        self.x = x
        self.y = y
        self.Token = Token
        self.dead = False
    
    def getPosition(self):
        return (self.x,self.y)
    
    def getToken(self):
        return self.Token
        
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.getToken() == other.getToken()
    
    def updatePosition(self,x,y):
        self.x = x
        self.y = y
    
    
class Move:
    '''Responsible for storing the data about a single move in the game
    Variables:
    fromSpot
    to
    
    '''
    def __init__(self,fromSpot,toSpot):
        self.fromSpot = fromSpot
        self.toSpot = toSpot
        
    def __eq__(self,other):
        if other == None:
            return False
        return self.fromSpot == other.fromSpot and self.toSpot == other.toSpot
    
    def __str__(self):
        return str(self.fromSpot[0])+","+str(self.fromSpot[1])+" "+str(self.toSpot[0])+","+str(self.toSpot[1])
        
        