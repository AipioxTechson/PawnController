class Game:
    """Responsible for holding the state of the Game.
    Variables:
    grid
    turn
    player_one
    player_two
    Functions:
    isWin()
    nextMove()
    printState()
    ApplyMove()
    """

    def __init__(self,player1: "Player" ,player2: "Player", grid = []):
        self.grid = grid
        self.turn = 0
        self.player_one = player1
        self.player_two = player2
    
    def isWin(self):
        isWinner = False
        player1Winner = True
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
        if all([1 if self.player_one.getAvailableMoves(piece) == [] else 0 for piece in self.player_one.getPieces()]):
            isWinner = True
            player1Winner = self.turn % 2 == 0
            
        if isWinner:
            self.player_one.processData(player1Winner)
            self.player_two.processData(not player1Winner)
            return True
        return False
    
    def nextMove(self):
        if self.turn % 2 == 0:
            self.turn = 1
            return self.player_one.nextMove()
        self.turn = 0
        return self.player_two.nextMove()
    
    def ApplyMove(self,Move,player):
        fromX,fromY = Move.fromSpot
        toX,toY = Move.toSpot
        self.grid[toX][toY] = self.grid[fromX][fromY]
        self.grid[fromX][fromY] = Piece(fromX,fromY," ")
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
                
            
class Piece:
    '''Responsible for holding the data about a single Piece in the game.
    Variables:
    x
    y
    Token
    dead
    Functions:
    getPosition()
    getToken()
    isDead()
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
    
    def isDead(self):
        return self.dead
    
    
    
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
        return self.fromSpot == other.fromSpot and self.toSpot == other.toSpot
        
        