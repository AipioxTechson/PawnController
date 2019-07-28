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
    
    """

    def __init__(self,player1: "Player" ,player2: "Player", grid = []):
        self.grid = grid
        self.turn = 0
        self.player_one = player1
        self.player_two = player2
    
    def isWin(self):
        pass
    
    def nextMove(self):
        pass
    
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
    Functions:
    getPosition()
    getToken()
    '''
    def __init__(self,x,y,Token):
        self.x = x
        self.y = y
        self.Token = Token
    
    def getPosition(self):
        return (x,y)
    
    def getToken(self):
        return self.Token
    
        